from django.shortcuts import render
from django.views.generic import ListView
from warhammer.models import Campagne

# Create your views here.
def homeview(request):
    return render(request, "warhamTemplate/campagne/details/campaigns_list.html")


##################### Reads views #####################
class WarhamCampaignListView(ListView):
    model = Campagne
    template_name = "warhamTemplate/campagne/details/campaigns_list.html"

    def get_context_data(self, **kwargs):
        context = {}
        campagnes_warhammer = Campagne.objects.all()
        # personnage_warhammer = Player.objects.all()
        context["campagnes_warhammer"] = campagnes_warhammer
        # context["personnage_warhammer"] = personnage_warhammer
        return super().get_context_data(**context)
