from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect

from django.template import RequestContext

# Create your views here.
@login_required
def gg_entry(request):
    return render_to_response('main.html', { })
