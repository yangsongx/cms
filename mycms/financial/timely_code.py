# Run under Celery 4.2, 4.3
# Remember you MUST run the worker(physical code of exeuctie task)
# Then launch the beat, i.e, both of them are needed.
#
import requests
import datetime
from celery import Celery
from celery.schedules import crontab

import os

financial_list = [
     # name   code   totally    counts
    {'name':'华夏上证ETF', 'code':'510630' , 'sum': 1000.00, 'counts': 823.17},
    {'name':'华夏成长', 'code':'000001' , 'sum': 22122.23, 'counts': 22301.68},
    {'name':'广发消费混合', 'code':'270041' , 'sum': 2000.00, 'counts': 2000.00},
#    {'name':'南方成长Ａ', 'code':'202023' , 'sum': 4290.09, 'counts': 1845.01},
    {'name':'南方成长Ａ', 'code':'202023' , 'sum': 6290.09, 'counts': 2814.47},
]


class HeXun:
    __leading_url = 'http://jingzhi.funds.hexun.com/'
    __yesterday = '1970-01-01'
    __txtfn = 'report.txt'

    def __init__(self):
        self.__yesterday = (datetime.datetime.now() - datetime.timedelta(days = 1))\
                           .strftime("%Y-%m-%d")

    def fetch_jsdata(self):
        url = 'http://jingzhi.funds.hexun.com/jz/JsonData/kaifangjingz.aspx?callback=callback&sortType=down'
        res = requests.get(url)
        res_data = res.text

        ret = re.search(r'^callback\((.*)\)$', res_data)
        if ret != None:
            return json.loads(ret.group(1))
        else:
            return None

    def start(self):
        print("==begin collect data==")
        jsdata = self.fetch_jsdata()
        if jsdata == None:
            print("===== Error, blank JSON data found from the web")
            return -1

#        print(json.dumps(jsdata, indent=2))

        for it in financial_list:
            print("==Go!")
            self.extract_price(it, jsdata)

        self.dump_data()


    def extract_price(self, item, jsdata):
        for i in jsdata['list']:
            if i['fundCode'] == item['code']:
                item['price'] = float(i['tNet'])
                item['when'] = jsdata['today']
                break

        return 0

    def extract_price2(self, item):
        url = self.__leading_url + item['code'] + '.shtml'
        res = requests.get(url)
        res_data = res.text


        html = etree.HTML(res_data)
        ret = html.xpath('//div[@class="top_right"]/table/tbody/tr/td')

        print("=====")
        print(ret[0].tag)
        print(ret[0].text)
        print(ret[1].tag)
        print(ret[1].text)

        item['when'] = ret[0].text
        item['price'] = float(ret[1].text)
        return 0

    def dump_data(self):
        for it in financial_list:
            print(json.dumps(it, indent = 2, ensure_ascii = False))


app = Celery('timely-task', broker='redis://localhost:6379/0')


@app.on_after_configure.connect
def setup_timely_task(sender, **kwargs):
    print("connect and configed OK")
    sender.add_periodic_task(10, go.s('hello'), name = 'every 10 sec')

    # Daily report
    sender.add_periodic_task(
        crontab(minute = 30, hour=9, day_of_week= [2,3,4,5,6]),
        collect_daily_data.s('useless param'),
        name = 'jijing collection')

#class celery.schedules.crontab(minute='*', hour='*', day_of_week='*', day_of_month='*', month_of_year='*', **kwargs)


@app.task
def go(arg):
    print("The timely task, with %s data" %(arg))
    h = HeXun()
    h.start()

@app.task
def collect_daily_data(arg):
    # Try extract the jijin data...
    print("The timely task, with %s data" %(arg))
