from django.urls import reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from warhammer.models import (
    Campagne,
    Player,
    PointDeBlessure,
    PointDeDestin,
    PlanCarriere,
    Equipement,
    ExperiencePersonnage,
    DescriptionPersonnelle,
    CaracteristiqueActuelle,
    CaracteristiqueBase,
    ArmeContact,
    ArmeDistance,
    Armure,
    Bourse,
    Magie,
    Monture,
    Sortilege,
    Competence,
)
from warhammer.forms import (
    NewWarhammerPlayerForm,
    NewCaracteristiqueBaseForm,
    NewPlanCarriereForm,
    NewCaracteristiqueActuelleForm,
    NewCompetenceForm,
    NewEquipementForm,
    NewDescriptionPersonnelleForm,
    NewArmeContactForm,
    NewArmeDistanceForm,
    NewArmureForm,
    NewMagieForm,
    NewBourseForm,
    NewMontureForm,
    NewExperiencePersonnageForm,
    NewWarhammerCampagneForm,
    NewPointDeBlessureForm,
    NewPointDeDestinForm,
    NewSortilegeForm,
)
from warhammer.utils import (
    list_players_attak_rank,
    dict_players_attak_rank,
    format_dict_players_attak_rank,
    get_actual_carriere,
)

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


class WarhamPlayerCampagneUpdate(UpdateView):
    """"""

    model = Player
    fields = ["campagne"]
    template_name = "warhamTemplate/player/update/player_campagne_update.html"

    def get_success_url(self):
        player = Player.objects.get(id=self.kwargs["pk"])
        return reverse("warhammer:details_personnages", kwargs={"pk": player.id})


class WarhamPlanCarriereUpdateView(UpdateView):
    """"""

    model = PlanCarriere
    form_class = NewPlanCarriereForm
    template_name = "player/update/planCarriere_update.html"

    def get_context_data(self, **kwargs):
        context = {}
        planCarriere_update = PlanCarriere.objects.get(id=self.kwargs["pk"])
        context["planCarriere_update"] = planCarriere_update
        return super().get_context_data(**context)

    def get_success_url(self):
        plan_carriere = PlanCarriere.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=plan_carriere.player.id)
        return reverse("warhammer:details_personnages", kwargs={"pk": player.id})


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


class WarhamCompetenceDeleteViews(DeleteView):
    """"""

    model = Competence
    context_object_name = "delete_competence"
    template_name = "warhamTemplate/player/delete/competence_delete.html"

    def get_success_url(self):
        competence = Competence.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=competence.player.id)
        return reverse("warhammer:details_personnages", kwargs={"pk": player.id})


class WarhamArmeContactDeleteViews(DeleteView):
    """"""

    model = ArmeContact
    context_object_name = "delete_arme_contact"
    template_name = "warhamTemplate/player/delete/armeContact_delete.html"

    def get_success_url(self):
        arme_contact = ArmeContact.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=arme_contact.player.id)
        return reverse("warhammer:details_personnages", kwargs={"pk": player.id})


class WarhamArmeDistanceDeleteViews(DeleteView):
    """"""

    model = ArmeDistance
    context_object_name = "delete_arme_distance"
    template_name = "warhamTemplate/player/delete/armeDistance_delete.html"

    def get_success_url(self):
        arme_distance = ArmeDistance.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=arme_distance.player.id)
        return reverse("warhammer:details_personnages", kwargs={"pk": player.id})


class WarhamArmureDeleteViews(DeleteView):
    """"""

    model = Armure
    context_object_name = "delete_armure"
    template_name = "warhamTemplate/player/delete/armure_delete.html"

    def get_success_url(self):
        armure = Armure.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=armure.player.id)
        return reverse("warhammer:details_personnages", kwargs={"pk": player.id})


class WarhamEquipementDeleteViews(DeleteView):
    """"""

    model = Equipement
    context_object_name = "delete_equipement"
    template_name = "warhamTemplate/player/delete/equipement_delete.html"

    def get_success_url(self):
        equipement = Equipement.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=equipement.player.id)
        return reverse("warhammer:details_personnages", kwargs={"pk": player.id})


class WarhamBourseDeleteViews(DeleteView):
    """"""

    model = Bourse
    context_object_name = "delete_bourse"
    template_name = "warhamTemplate/player/delete/bourse_delete.html"

    def get_success_url(self):
        bourse = Bourse.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=bourse.player.id)
        return reverse("warhammer:details_personnages", kwargs={"pk": player.id})


class WarhamMontureDeleteViews(DeleteView):
    """ """

    model = Monture
    context_object_name = "delete_monture"
    template_name = "monture/delete/monture_delete.html"

    def get_success_url(self):
        monture = Monture.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=monture.player.id)
        return reverse("warhammer:details_monture", kwargs={"pk": player.id})
