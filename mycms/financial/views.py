from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from financial.models import Investment

# Create your views here.

def summary_entry(request):
    # First, process the data.
    try:
        obj = Investment.objects.all()
        totally_money = 0.0

        for it in obj:
            totally_money = totally_money + it.base_money

        print("There are totally %.2f money" %(totally_money))
    except:
        return HttpResponse("exception met for this action")
   

    return render(request, 'sum.html', {"mymoney": 45, "trows": 34})

