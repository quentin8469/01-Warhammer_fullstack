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


class WarhamArmeContactUpdateView(UpdateView):
    """"""

    model = ArmeContact
    form_class = NewArmeContactForm
    template_name = "warhamTemplate/player/update/armeContact_update.html"

    def get_context_data(self, **kwargs):
        context = {}
        arme_contact_update = ArmeContact.objects.get(id=self.kwargs["pk"])
        context["armes_contact"] = arme_contact_update

        return super().get_context_data(**context)

    def get_success_url(self):
        arme_contact = ArmeContact.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=arme_contact.player.id)
        return reverse("warhammer:details_personnages", kwargs={"pk": player.id})


class WarhamArmeDistanceUpdateView(UpdateView):
    """"""

    model = ArmeDistance
    form_class = NewArmeDistanceForm
    template_name = "warhamTemplate/player/update/armeDistance_update.html"

    def get_context_data(self, **kwargs):
        context = {}
        arme_distance_update = ArmeDistance.objects.get(id=self.kwargs["pk"])
        context["armes_distance"] = arme_distance_update

        return super().get_context_data(**context)

    def get_success_url(self):
        arme_distance = ArmeDistance.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=arme_distance.player.id)
        return reverse("warhammer:details_personnages", kwargs={"pk": player.id})


class WarhamArmureUpdateView(UpdateView):
    """"""

    model = Armure
    form_class = NewArmureForm
    template_name = "warhamTemplate/player/update/armure_update.html"

    def get_context_data(self, **kwargs):
        context = {}
        armure_update = Armure.objects.get(id=self.kwargs["pk"])
        context["armure_update"] = armure_update

        return super().get_context_data(**context)

    def get_success_url(self):
        armure = Armure.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=armure.player.id)
        return reverse("warhammer:details_personnages", kwargs={"pk": player.id})


class WarhamCompetenceUpdateView(UpdateView):
    """"""

    model = Competence
    form_class = NewCompetenceForm
    template_name = "warhamTemplate/player/update/competence_update.html"

    def get_context_data(self, **kwargs):
        context = {}
        competence_update = Competence.objects.get(id=self.kwargs["pk"])
        context["competence_update"] = competence_update

        return super().get_context_data(**context)

    def get_success_url(self):
        competence = Competence.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=competence.player.id)
        return reverse("warhammer:details_personnages", kwargs={"pk": player.id})


class WarhamEquipementUpdateView(UpdateView):
    """"""

    model = Equipement
    form_class = NewEquipementForm
    template_name = "warhamTemplate/player/update/equipement_update.html"

    def get_context_data(self, **kwargs):
        context = {}
        equipement_update = Equipement.objects.get(id=self.kwargs["pk"])
        context["equipement_update"] = equipement_update

        return super().get_context_data(**context)

    def get_success_url(self):
        equipement = Equipement.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=equipement.player.id)
        return reverse("warhammer:details_personnages", kwargs={"pk": player.id})


class WarhamBourseUpdateView(UpdateView):
    """"""

    model = Bourse
    form_class = NewBourseForm
    template_name = "warhamTemplate/player/update/bourse_update.html"

    def get_context_data(self, **kwargs):
        context = {}
        bourse_update = Bourse.objects.get(id=self.kwargs["pk"])
        context["bourse_update"] = bourse_update
        return super().get_context_data(**context)

    def get_success_url(self):
        bourse = Bourse.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=bourse.player.id)
        return reverse("warhammer:details_personnages", kwargs={"pk": player.id})


class WarhamPlanCarriereUpdateView(UpdateView):
    """"""

    model = PlanCarriere
    form_class = NewPlanCarriereForm
    template_name = "warhamTemplate/player/update/planCarriere_update.html"

    def get_context_data(self, **kwargs):
        context = {}
        planCarriere_update = PlanCarriere.objects.get(id=self.kwargs["pk"])
        context["planCarriere_update"] = planCarriere_update
        return super().get_context_data(**context)

    def get_success_url(self):
        plan_carriere = PlanCarriere.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=plan_carriere.player.id)
        return reverse("warhammer:details_personnages", kwargs={"pk": player.id})


class WarhamCaracteristiqueActuelleUpdateView(UpdateView):
    """"""

    model = CaracteristiqueActuelle
    form_class = NewCaracteristiqueActuelleForm
    template_name = "player/update/carriereActuelle_update.html"

    def get_context_data(self, **kwargs):
        context = {}
        carriere_actuelle_update = CaracteristiqueActuelle.objects.get(
            id=self.kwargs["pk"]
        )
        context["carriere_actuelle_update"] = carriere_actuelle_update
        return super().get_context_data(**context)

    def get_success_url(self):
        carriere_actuelle = CaracteristiqueActuelle.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=carriere_actuelle.player.id)
        return reverse("warhammer:details_personnages", kwargs={"pk": player.id})


class WarhamPlanCarriereUpdateView(UpdateView):
    """"""

    model = PlanCarriere
    form_class = NewPlanCarriereForm
    template_name = "warhamTemplate/player/update/planCarriere_update.html"

    def get_context_data(self, **kwargs):
        context = {}
        planCarriere_update = PlanCarriere.objects.get(id=self.kwargs["pk"])
        context["planCarriere_update"] = planCarriere_update
        return super().get_context_data(**context)

    def get_success_url(self):
        plan_carriere = PlanCarriere.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=plan_carriere.player.id)
        return reverse("warhammer:details_personnages", kwargs={"pk": player.id})


class WarhamExperienceUpdateView(UpdateView):
    """"""

    model = ExperiencePersonnage
    form_class = NewExperiencePersonnageForm
    template_name = "warhamTemplate/player/update/experience_update.html"

    def get_context_data(self, **kwargs):
        context = {}
        experience_update = ExperiencePersonnage.objects.get(id=self.kwargs["pk"])
        context["experience_update"] = experience_update
        return super().get_context_data(**context)

    def get_success_url(self):
        experience = ExperiencePersonnage.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=experience.player.id)
        return reverse("warhammer:details_personnages", kwargs={"pk": player.id})


class WarhamDetailsDescriptionPersonnageUpdateView(View):
    """"""

    player_model = Player
    description_model = DescriptionPersonnelle
    player_form_class = NewWarhammerPlayerForm
    description_form_class = NewDescriptionPersonnelleForm
    template_name = "warhamTemplate/player/update/details_perso_update.html"

    def get(self, request, *args, **kwargs):
        player = get_object_or_404(self.player_model, pk=self.kwargs["pk"])
        player_form = self.player_form_class(instance=player)
        description, created = self.description_model.objects.get_or_create(
            player_id=player
        )
        description_form = self.description_form_class(instance=description)
        return render(
            request,
            self.template_name,
            {
                "player_form": player_form,
                "description_form": description_form,
                "player_id": player.id,
            },
        )

    def post(self, request, *args, **kwargs):
        player = get_object_or_404(self.player_model, pk=self.kwargs["pk"])
        player_form = self.player_form_class(request.POST, instance=player)
        description, created = self.description_model.objects.get_or_create(
            player_id=player
        )
        description_form = self.description_form_class(
            request.POST, request.FILES, instance=description
        )

        if player_form.is_valid() and description_form.is_valid():
            player_form.save()
            description_form.save()
            return redirect("warhammer:details_personnages", pk=player.id)
        else:
            print("Les formulaires sont invalides!")

        return render(
            request,
            self.template_name,
            {
                "player_form": player_form,
                "description_form": description_form,
                "player_id": player.id,
            },
        )


class WarhamMontureUpdateView(UpdateView):
    """"""

    model = Monture
    form_class = NewMontureForm
    template_name = "warhamTemplate/monture/update/monture_update.html"

    def get_context_data(self, **kwargs):
        context = {}
        monture_update = Monture.objects.get(id=self.kwargs["pk"])
        context["monture_update"] = monture_update
        return super().get_context_data(**context)

    def get_success_url(self):
        monture = Monture.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=monture.player.id)
        return reverse("warhammer:details_monture", kwargs={"pk": player.id})


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
