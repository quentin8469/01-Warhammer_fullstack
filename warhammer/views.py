from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    View,
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


class WarhamPlayerCreateView(View):
    template_name = "warhamTemplate/player/create/player_create.html"

    def get(self, request):
        form1 = NewWarhammerPlayerForm(prefix="form1")
        form2 = NewCaracteristiqueBaseForm(prefix="form2")
        form3 = NewPlanCarriereForm(prefix="form3")
        form4 = NewCaracteristiqueActuelleForm(prefix="form4")
        form5 = NewCompetenceForm(prefix="form5")
        form6 = NewEquipementForm(prefix="form6")
        form7 = NewDescriptionPersonnelleForm(prefix="form7")
        form8 = NewArmeContactForm(prefix="form8")
        form9 = NewArmeDistanceForm(prefix="form9")
        form10 = NewArmureForm(prefix="form10")
        # form11 = NewMagieForm(prefix="form11")
        form12 = NewBourseForm(prefix="form12")
        # form13 = NewMontureForm(prefix="form13")
        form14 = NewExperiencePersonnageForm(prefix="form14")
        form15 = NewWarhammerCampagneForm(prefix="form15")
        form16 = NewPointDeBlessureForm(prefix="form16")
        form17 = NewPointDeDestinForm(prefix="form17")
        # form18 = NewSortilegeForm(prefix="form18")
        return render(
            request,
            self.template_name,
            {
                "form1": form1,
                "form2": form2,
                "form3": form3,
                "form4": form4,
                "form5": form5,
                "form6": form6,
                "form7": form7,
                "form8": form8,
                "form9": form9,
                "form10": form10,
                # "form11": form11,
                "form12": form12,
                # "form13": form13,
                "form14": form14,
                "form15": form15,
                "form16": form16,
                "form17": form17,
            },
        )

    def post(self, request):
        form1 = NewWarhammerPlayerForm(request.POST, prefix="form1")
        form2 = NewCaracteristiqueBaseForm(request.POST, prefix="form2")
        form3 = NewPlanCarriereForm(request.POST, prefix="form3")
        form4 = NewCaracteristiqueActuelleForm(request.POST, prefix="form4")
        form5 = NewCompetenceForm(request.POST, prefix="form5")
        form6 = NewEquipementForm(request.POST, prefix="form6")
        form7 = NewDescriptionPersonnelleForm(request.POST, prefix="form7")
        form8 = NewArmeContactForm(request.POST, prefix="form8")
        form9 = NewArmeDistanceForm(request.POST, prefix="form9")
        form10 = NewArmureForm(request.POST, prefix="form10")
        form12 = NewBourseForm(request.POST, prefix="form12")
        form14 = NewExperiencePersonnageForm(request.POST, prefix="form14")
        form16 = NewPointDeBlessureForm(request.POST, prefix="form16")
        form17 = NewPointDeDestinForm(request.POST, prefix="form17")

        if form1.is_valid():
            model1 = form1.save(commit=False)
            model1.joueur = self.request.user
            model1.save()
            model2 = form2.save(commit=False)
            model2.player = Player.objects.get(id=model1.id)
            model2.save()
            model3 = form3.save(commit=False)
            model3.player = Player.objects.get(id=model1.id)
            model3.save()
            model4 = form4.save(commit=False)
            model4.player = Player.objects.get(id=model1.id)
            model4.save()
            model5 = form5.save(commit=False)
            model5.player = Player.objects.get(id=model1.id)
            model5.save()
            model6 = form6.save(commit=False)
            model6.player = Player.objects.get(id=model1.id)
            model6.save()
            model7 = form7.save(commit=False)
            model7.player = Player.objects.get(id=model1.id)
            model7.save()
            model8 = form8.save(commit=False)
            model8.player = Player.objects.get(id=model1.id)
            model8.save()
            model9 = form9.save(commit=False)
            model9.player = Player.objects.get(id=model1.id)
            model9.save()
            model10 = form10.save(commit=False)
            model10.player = Player.objects.get(id=model1.id)
            model10.save()
            model12 = form12.save(commit=False)
            model12.player = Player.objects.get(id=model1.id)
            model12.save()
            model14 = form14.save(commit=False)
            model14.player = Player.objects.get(id=model1.id)
            model14.save()
            model16 = form16.save(commit=False)
            model16.player = Player.objects.get(id=model1.id)
            model16.save()
            model17 = form17.save(commit=False)
            model17.player = Player.objects.get(id=model1.id)
            model17.save()

            return HttpResponseRedirect(reverse("warhammer:liste_campagne"))
        else:
            return render(
                request,
                self.template_name,
                {
                    "form1": form1,
                    "form2": form2,
                    "form3": form3,
                    "form4": form4,
                    "form5": form5,
                    "form6": form6,
                    "form7": form7,
                    "form8": form8,
                    "form9": form9,
                    "form10": form10,
                    "form12": form12,
                    "form14": form14,
                    "form16": form16,
                    "form17": form17,
                },
            )


class WarhamArmeContactCreateView(CreateView):
    """"""

    model = ArmeContact
    form_class = NewArmeContactForm
    template_name = "warhamTemplate/player/create/armeContact_create.html"

    def form_valid(self, form):
        form.instance.player = Player.objects.get(id=self.kwargs["pk"])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = {}
        player = Player.objects.get(id=self.kwargs["pk"])
        context["player"] = player
        return super().get_context_data(**context)

    def get_success_url(self):
        return reverse(
            "warhammer:details_personnages", kwargs={"pk": self.kwargs["pk"]}
        )


class WarhamArmeDistanceCreateView(CreateView):
    """"""

    model = ArmeDistance
    form_class = NewArmeDistanceForm
    template_name = "warhamTemplate/player/create/armeDistance_create.html"

    def form_valid(self, form):
        form.instance.player = Player.objects.get(id=self.kwargs["pk"])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = {}
        player = Player.objects.get(id=self.kwargs["pk"])
        context["player"] = player
        return super().get_context_data(**context)

    def get_success_url(self):
        return reverse(
            "warhammer:details_personnages", kwargs={"pk": self.kwargs["pk"]}
        )


class WarhamArmureCreateView(CreateView):
    """"""

    model = Armure
    form_class = NewArmureForm
    template_name = "warhamTemplate/player/create/armure_create.html"

    def form_valid(self, form):
        form.instance.player = Player.objects.get(id=self.kwargs["pk"])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = {}
        player = Player.objects.get(id=self.kwargs["pk"])
        context["player"] = player
        return super().get_context_data(**context)

    def get_success_url(self):
        return reverse(
            "warhammer:details_personnages", kwargs={"pk": self.kwargs["pk"]}
        )


class WarhamCompetenceCreateView(CreateView):
    """"""

    model = Competence
    form_class = NewCompetenceForm
    template_name = "warhamTemplate/player/create/competence_create.html"

    def form_valid(self, form):
        form.instance.player = Player.objects.get(id=self.kwargs["pk"])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = {}
        player = Player.objects.get(id=self.kwargs["pk"])
        context["player"] = player
        return super().get_context_data(**context)

    def get_success_url(self):
        return reverse(
            "warhammer:details_personnages", kwargs={"pk": self.kwargs["pk"]}
        )


class WarhamEquipementCreateView(CreateView):
    """"""

    model = Equipement
    form_class = NewEquipementForm
    template_name = "warhamTemplate/player/create/equipement_create.html"

    def form_valid(self, form):
        form.instance.player = Player.objects.get(id=self.kwargs["pk"])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = {}
        player = Player.objects.get(id=self.kwargs["pk"])
        context["player"] = player
        return super().get_context_data(**context)

    def get_success_url(self):
        return reverse(
            "warhammer:details_personnages", kwargs={"pk": self.kwargs["pk"]}
        )


class WarhamBourseCreateView(CreateView):
    """"""

    model = Bourse
    form_class = NewBourseForm
    template_name = "warhamTemplate/player/create/bourse_create.html"

    def form_valid(self, form):
        form.instance.player = Player.objects.get(id=self.kwargs["pk"])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = {}
        player = Player.objects.get(id=self.kwargs["pk"])
        context["player"] = player
        return super().get_context_data(**context)

    def get_success_url(self):
        return reverse(
            "warhammer:details_personnages", kwargs={"pk": self.kwargs["pk"]}
        )


class WarhamPlanCarriereCreateView(CreateView):
    """ """

    model = PlanCarriere
    form_class = NewPlanCarriereForm
    template_name = "warhamTemplate/player/create/planCarriere_create.html"

    def form_valid(self, form):
        form.instance.player = Player.objects.get(id=self.kwargs["pk"])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = {}
        player = Player.objects.get(id=self.kwargs["pk"])
        context["player"] = player
        return super().get_context_data(**context)

    def get_success_url(self):
        return reverse(
            "warhammer:details_personnages", kwargs={"pk": self.kwargs["pk"]}
        )


class WarhamMontureCreateView(CreateView):
    """"""

    model = Monture
    form_class = NewMontureForm
    template_name = "warhamTemplate/monture/create/monture_create.html"

    def form_valid(self, form):
        form.instance.player = Player.objects.get(id=self.kwargs["pk"])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = {}
        player = Player.objects.get(id=self.kwargs["pk"])
        context["player"] = player
        return super().get_context_data(**context)

    def get_success_url(self):
        return reverse("warhammer:details_monture", kwargs={"pk": self.kwargs["pk"]})


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


class WarhamPlayerDetailView(DetailView):
    """class pour afficher les détails d'un personnage joueur warhammer"""

    model = Player
    template_name = "warhamTemplate/player/details/player_details.html"

    def get_context_data(self, **kwargs):
        context = {}
        try:
            personnage = Player.objects.get(id=self.kwargs["pk"])
            profil_initial = CaracteristiqueBase.objects.get(player=self.kwargs["pk"])
            plan_carrieres = PlanCarriere.objects.filter(player=self.kwargs["pk"])
            profil_actuel = CaracteristiqueActuelle.objects.get(
                player=self.kwargs["pk"]
            )
            experience = ExperiencePersonnage.objects.get(player=self.kwargs["pk"])
            description = DescriptionPersonnelle.objects.get(id=self.kwargs["pk"])
            competences = Competence.objects.filter(player=self.kwargs["pk"])
            equipements = Equipement.objects.filter(player=self.kwargs["pk"])
            armes_contacts = ArmeContact.objects.filter(player=self.kwargs["pk"])
            armes_distances = ArmeDistance.objects.filter(player=self.kwargs["pk"])
            armures_player = Armure.objects.filter(player=self.kwargs["pk"])
            bourse = Bourse.objects.get(player=self.kwargs["pk"])
            blessures = PointDeBlessure.objects.get(player=self.kwargs["pk"])
            destin = PointDeDestin.objects.get(player=self.kwargs["pk"])
            # get dict of all initiative by attaque
            player_campagne = Player.objects.filter(campagne=personnage.campagne.id)
            carac_actu_player = []
            for player in player_campagne:
                carac_actu = CaracteristiqueActuelle.objects.get(player=player.id)
                carac_actu_player.append(carac_actu)
            list_attak_rank = list_players_attak_rank(carac_actu_player)
            dict_attak_rank = dict_players_attak_rank(list_attak_rank)
            format_dict_attak_rank = format_dict_players_attak_rank(dict_attak_rank)
            # get the last carriere in plan_carrieres
            last_carrriere = get_actual_carriere(plan_carrieres)
            # details player view contexts
            context["personnage"] = personnage
            context["experience"] = experience
            context["bourse"] = bourse
            context["blessures"] = blessures
            context["destin"] = destin
            context["description"] = description
            context["competences"] = competences
            context["profil_initial"] = profil_initial
            context["profil_actuel"] = profil_actuel
            context["plan_carrieres"] = plan_carrieres
            context["armes_contacts"] = armes_contacts
            context["armes_distances"] = armes_distances
            context["equipements"] = equipements
            context["dict_attak_rank"] = format_dict_attak_rank
            context["armures"] = armures_player
            context["carriere_actuelle"] = last_carrriere[-1]
        except:
            personnage = Player.objects.get(id=self.kwargs["pk"])
            profil_initial = CaracteristiqueBase.objects.get(player=self.kwargs["pk"])
            plan_carrieres = PlanCarriere.objects.filter(player=self.kwargs["pk"])
            profil_actuel = CaracteristiqueActuelle.objects.get(
                player=self.kwargs["pk"]
            )
            experience = ExperiencePersonnage.objects.get(player=self.kwargs["pk"])
            description = DescriptionPersonnelle.objects.get(id=self.kwargs["pk"])
            competences = Competence.objects.filter(player=self.kwargs["pk"])
            equipements = Equipement.objects.filter(player=self.kwargs["pk"])
            armes_contacts = ArmeContact.objects.filter(player=self.kwargs["pk"])
            armes_distances = ArmeDistance.objects.filter(player=self.kwargs["pk"])
            armures_player = Armure.objects.filter(player=self.kwargs["pk"])
            bourse = Bourse.objects.get(player=self.kwargs["pk"])
            blessures = PointDeBlessure.objects.get(player=self.kwargs["pk"])
            destin = PointDeDestin.objects.get(player=self.kwargs["pk"])
            last_carrriere = get_actual_carriere(plan_carrieres)
            # details player view contexts
            context["personnage"] = personnage
            context["experience"] = experience
            context["blessures"] = blessures
            context["destin"] = destin
            context["bourse"] = bourse
            context["description"] = description
            context["competences"] = competences
            context["profil_initial"] = profil_initial
            context["profil_actuel"] = profil_actuel
            context["plan_carrieres"] = plan_carrieres
            context["armes_contacts"] = armes_contacts
            context["armes_distances"] = armes_distances
            context["equipements"] = equipements
            context["armures"] = armures_player
            context["carriere_actuelle"] = last_carrriere[-1]
        return super().get_context_data(**context)


class WarhamMontureListView(ListView):
    """ """

    model = Monture
    template_name = "warhamTemplate/monture/details/monture_details.html"

    def get_context_data(self, **kwargs):
        context = {}
        montures = Monture.objects.filter(player=self.kwargs["pk"])
        personnage = Player.objects.get(id=self.kwargs["pk"])
        context["montures"] = montures
        context["personnage"] = personnage
        return super().get_context_data(**context)


class WarhamMagieListView(ListView):
    """ """

    model = Magie
    template_name = "warhamTemplate/magie/details/magie_details.html"

    def get_context_data(self, **kwargs):
        context = {}
        personnage = Player.objects.get(id=self.kwargs["pk"])
        magies = Magie.objects.get(player=self.kwargs["pk"])
        sortileges = Sortilege.objects.filter(player=self.kwargs["pk"])
        magies_mineurs = sortileges.filter(type_magie="Magie mineure")
        magies_batailles = sortileges.filter(type_magie="Magie de bataille")
        magies_demoniques = sortileges.filter(type_magie="Magie démonique")
        magies_druidiques = sortileges.filter(type_magie="Magie druidique")
        magies_elementaires = sortileges.filter(type_magie="Magie elementaire")
        magies_illusoires = sortileges.filter(type_magie="Magie illusoire")
        magies_necromantiques = sortileges.filter(type_magie="Magie necromantique")
        magies_autres = sortileges.filter(type_magie="Magie autre")
        print(magies)
        print(sortileges)
        context["personnage"] = personnage
        context["magies"] = magies
        context["sortileges"] = sortileges
        context["magies_mineurs"] = magies_mineurs
        context["magies_batailles"] = magies_batailles
        context["magies_demoniques"] = magies_demoniques
        context["magies_druidiques"] = magies_druidiques
        context["magies_elementaires"] = magies_elementaires
        context["magies_illusoires"] = magies_illusoires
        context["magies_necromantiques"] = magies_necromantiques
        context["magies_autres"] = magies_autres
        return super().get_context_data(**context)


class WarhamSortilegeListView(ListView):
    """ """

    model = Sortilege
    template_name = "warhamTemplate/magie/details/magie_mineure_details.html"

    def get_context_data(self, **kwargs):
        context = {}
        personnage = Player.objects.get(id=self.kwargs["pk"])
        sortileges = Sortilege.objects.filter(player=self.kwargs["pk"])
        magies_mineurs = sortileges.filter(type_magie="Magie mineure")
        magies_batailles = sortileges.filter(type_magie="Magie de bataille")
        magies_demoniques = sortileges.filter(type_magie="Magie démonique")
        magies_druidiques = sortileges.filter(type_magie="Magie druidique")
        magies_elementaires = sortileges.filter(type_magie="Magie elementaire")
        magies_illusoires = sortileges.filter(type_magie="Magie illusoire")
        magies_necromantiques = sortileges.filter(type_magie="Magie necromantique")
        magies_autres = sortileges.filter(type_magie="Magie autre")
        context["personnage"] = personnage
        context["sortileges"] = sortileges
        context["magies_mineurs"] = magies_mineurs
        context["magies_batailles"] = magies_batailles
        context["magies_demoniques"] = magies_demoniques
        context["magies_druidiques"] = magies_druidiques
        context["magies_elementaires"] = magies_elementaires
        context["magies_illusoires"] = magies_illusoires
        context["magies_necromantiques"] = magies_necromantiques
        context["magies_autres"] = magies_autres
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
    template_name = "warhamTemplate/player/update/carriereActuelle_update.html"

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


class WarhamPointDestinUpdateView(UpdateView):
    """"""

    model = PointDeDestin
    form_class = NewPointDeDestinForm
    template_name = "warhamTemplate/player/update/destin_update.html"

    def get_context_data(self, **kwargs):
        context = {}
        destin_update = PointDeDestin.objects.get(id=self.kwargs["pk"])
        context["destin_update"] = destin_update
        return super().get_context_data(**context)

    def get_success_url(self):
        destin = PointDeDestin.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=destin.player.id)
        return reverse("warhammer:details_personnages", kwargs={"pk": player.id})


class WarhamPointBlessureUpdateView(UpdateView):
    """"""

    model = PointDeBlessure
    form_class = NewPointDeBlessureForm
    template_name = "warhamTemplate/player/update/blessure_update.html"

    def get_context_data(self, **kwargs):
        context = {}
        blessure_update = PointDeBlessure.objects.get(id=self.kwargs["pk"])
        context["blessure_update"] = blessure_update
        return super().get_context_data(**context)

    def get_success_url(self):
        blessure = PointDeBlessure.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=blessure.player.id)
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
    template_name = "warhamTemplate/monture/delete/monture_delete.html"

    def get_success_url(self):
        monture = Monture.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=monture.player.id)
        return reverse("warhammer:details_monture", kwargs={"pk": player.id})
