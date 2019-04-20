from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from financial.models import Investment, MoneyDetails, Outcoming

import sys

# Create your views here.

# FIXME extract recent-12 months data...
def calculate_long_trend():
    # calculate on the N/A type money, for every month.

    # calculate on the non-N/A type money, for every month
    return 0


def calculate_how_much():
    result = 0.0

    obj = MoneyDetails.objects.values('fund').distinct()

    print(obj)
    print(len(obj))
    print("hello\n")

    for it in obj:
        print(it)
        print("try check the fund id %d" %(it['fund']))
        mobj = MoneyDetails.objects.filter(fund__id = it['fund']).order_by('-when')
        print(mobj)

        print(mobj[0].price * mobj[0].count)
        result = result + (mobj[0].price * mobj[0].count)

    print("=== end of dump details...")

    return result

# Entry point, for the HTML report
def summary_entry(request):
    # First, process the data.
    try:
        obj = Investment.objects.all()
        base_money = 0.0
        out_money = 0.0
        real_money = 0.0

        totally_money_gao = 0.0 # id-0
        totally_money_yang = 0.0 # id-1
        out_money_gao = 0.0
        out_money_yang = 0.0

        render_dict_data = {
        }

        for it in obj:
            base_money = base_money + it.base_money
            if it.who == 0:
                totally_money_gao = totally_money_gao + it.base_money
            else:
                totally_money_yang = totally_money_yang + it.base_money

        # Next, need substract the outcoming
        obj = Outcoming.objects.all()
        for it in obj:
            out_money = out_money + it.base_money
            if it.who == 0:
                out_money_gao = out_money_gao + it.base_money
            else:
                out_money_yang = out_money_yang + it.base_money

        print("the base:%f, the out:%f" %(base_money, out_money))
        base_money = base_money - out_money
        totally_money_gao = totally_money_gao - out_money_gao
        totally_money_yang = totally_money_yang - out_money_yang

        print("the delta: %.2f" %(base_money))
        print("So, there are totally %.2f money" %(base_money))


        # how much does it worth?
        real_money = calculate_how_much()

        real_money = float('%.2f' %(real_money))
        base_money = float('%.2f' %(base_money))
        totally_money_gao = float('%.2f' %(totally_money_gao))
        totally_money_yang = float('%.2f' %(totally_money_yang))

        render_dict_data['overview'] = {
            'base_money': base_money,
            'real_money': real_money,
            'base_money_gao': totally_money_gao,
            'base_money_yang': totally_money_yang
        }


    except:
        msg = '%s || %s' %(sys.exc_info()[0], sys.exc_info()[1])

        return HttpResponse("exception met for summary: %s" %(msg))
   

    return render(request, 'sum.html', render_dict_data)

