from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from warhammer.models import Campagne, Player
from warhammer.forms import NewWarhammerCampagneForm

# Create your views here.
# def homeview(request):
#     return render(request, "warhamTemplate/campagne/details/campaigns_list.html")


##################### creates views #####################
class WarhamCampaignCreateView(CreateView):
    """Class pour la creation d'une campagne warhammer"""

    model = Campagne
    form_class = NewWarhammerCampagneForm
    template_name = "warhamTemplate/campagne/create/campaigns_create.html"
    success_url = "/warhammer/"

    def form_valid(self, form):
        return super().form_valid(form)


##################### Reads/Lists views #####################
class WarhamCampaignListView(ListView):
    """Liste toute les campagnes existantes"""

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
    """Liste des personnages dans une campagne crée"""

    model = Player
    template_name = "warhamTemplate/campagne/liste/player_list.html"

    def get_context_data(self, **kwargs):
        context = {}
        personnages = Player.objects.filter(campagne=self.kwargs["pk"])
        context["personnages"] = personnages
        return super().get_context_data(**context)


class WarhamPlayerDetailView(DeleteView):
    """class pour afficher les détails d'un personnage joueur warhammer"""

    model = Player
    template_name = "warhamTemplate/player/details/player_details.html"

    def get_context_data(self, **kwargs):
        context = {}
        try:
            personnage = Player.objects.get(id=self.kwargs["pk"])
            # details player view contexts
            context["personnage"] = personnage
        except:
            personnage = Player.objects.get(id=self.kwargs["pk"])
            # details player view contexts
            context["personnage"] = personnage
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


class WarhamPlayerDeleteViews(DeleteView):
    """Suppression d'un joueur warhammer"""

    model = Player
    context_object_name = "player"
    template_name = "warhamTemplate/player/delete/player_delete.html"
    success_url = "/warhammer/"
