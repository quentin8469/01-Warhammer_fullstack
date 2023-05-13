from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def cthulhuhomeview(request):
    return render(request, "cthulhuTemplate/campagne/liste/home_cthulhu.html")
