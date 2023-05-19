from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from cthulhu.models import CampagneCthulhu, Investigateur


# Create your views here.
# @login_required
# def cthulhuhomeview(request):
#     return render(request, "cthulhuTemplate/campagne/liste/home_cthulhu.html")


##################### Reads/Lists views #####################
@method_decorator(login_required, name="dispatch")
class CthulhuCampaignListView(ListView):
    """Liste toute les campagnes existantes de Cthulhu"""

    model = CampagneCthulhu
    template_name = "cthulhuTemplate/campagne/liste/home_cthulhu.html"

    def get_context_data(self, **kwargs):
        context = {}
        campagnes_cthulhu = CampagneCthulhu.objects.all()
        investigateur_cthulhu = Investigateur.objects.all()
        context["campagnes_cthulhu"] = campagnes_cthulhu
        context["investigateur_cthulhu"] = investigateur_cthulhu
        return super().get_context_data(**context)


@method_decorator(login_required, name="dispatch")
class CthulhuInvestigateurDetailView(DetailView):
    """class pour afficher les détails d'un personnage joueur warhammer"""

    model = Investigateur
    template_name = "cthulhuTemplate/investigateur/details/investigateur_details.html"

    def get_context_data(self, **kwargs):
        context = {}
        try:
            investigateur = Investigateur.objects.get(id=self.kwargs["pk"])
            # details player view contexts
            context["investigateur"] = investigateur
        except:
            investigateur = Investigateur.objects.get(id=self.kwargs["pk"])
            # details player view contexts
            context["investigateur"] = investigateur
        return super().get_context_data(**context)
