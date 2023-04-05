from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homeview(request):
    return render(request, "homeTemplate/base/home_base.html")
