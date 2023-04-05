from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from warhammer.models import Campagne, Player
from warhammer.forms import NewWarhammerCampagneForm

# Create your views here.
# def homeview(request):
#     return render(request, "warhamTemplate/campagne/details/campaigns_list.html")


##################### creates views #####################
class WarhamCampaignCreateView(CreateView):
    """Class pour al creation d'une campagne warhammer"""

    model = Campagne
    form_class = NewWarhammerCampagneForm
    template_name = "warhamTemplate/campagne/create/campaigns_create.html"
    success_url = "/warhammer/"

    def form_valid(self, form):
        return super().form_valid(form)


##################### Reads views #####################
class WarhamCampaignListView(ListView):
    """Liste toute les campagne existante"""

    model = Campagne
    template_name = "warhamTemplate/campagne/details/campaigns_list.html"

    def get_context_data(self, **kwargs):
        context = {}
        campagnes_warhammer = Campagne.objects.all()
        personnage_warhammer = Player.objects.all()
        context["campagnes_warhammer"] = campagnes_warhammer
        context["personnage_warhammer"] = personnage_warhammer
        return super().get_context_data(**context)


class WarhamCampaignPlayerListView(ListView):
    """Liste des personnage dans un campagne crée"""

    model = Player
    template_name = "warhamTemplate/campagne/liste/player_list.html"

    def get_context_data(self, **kwargs):
        context = {}
        personnages = Player.objects.filter(campagne=self.kwargs["pk"])
        context["personnages"] = personnages
        return super().get_context_data(**context)


##################### Updates views #####################
class WarhamCampagneUpdateView(UpdateView):
    """Class pour l'update d'une campagne warhammer"""

    model = Campagne
    form_class = NewWarhammerCampagneForm
    template_name = "warhamTemplate/campagne/create/campaigns_create.html"
    success_url = "/warhammer/"


##################### Deletes views #####################
class WarhamCampagneDeleteViews(DeleteView):
    """Suppression d'une camapagne warhammer"""

    model = Campagne
    context_object_name = "campagne"
    template_name = "warhamTemplate/campagne/delete/campaigns_delete.html"
    success_url = "/warhammer/"
