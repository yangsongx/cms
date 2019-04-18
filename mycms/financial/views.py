from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from financial.models import Investment, MoneyDetails

import sys

# Create your views here.

def test_foo():
    obj = MoneyDetails.objects.distinct()
    print(obj)
    print(len(obj))
    print("hello\n")
    for it in obj:
        print(it.fund.name)
        print(it.price * it.count)

    return 0

def summary_entry(request):
    # First, process the data.
    try:
        test_foo()
        obj = Investment.objects.all()
        totally_money = 0.0
        real_money = 0.0

        totally_money_gao = 0.0 # id-0
        totally_money_yang = 0.0 # id-1

        render_dict_data = {
        }

        for it in obj:
            totally_money = totally_money + it.base_money

        # how much does it worth?

        print("There are totally %.2f money" %(totally_money))

    except:
        msg = '%s || %s' %(sys.exc_info()[0], sys.exc_info()[1])

        return HttpResponse("exception met for summary: %s" %(msg))
   

    return render(request, 'sum.html', {"mydic":{"mymoney": 20, "trows": 34}})

