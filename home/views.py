from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def homeview(request):
    return render(request, "homeTemplate/base/home_base.html")
