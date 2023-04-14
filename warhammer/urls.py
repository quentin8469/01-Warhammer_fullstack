from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from warhammer.views import (
    WarhamCampaignListView,
    WarhamCampaignPlayerListView,
    WarhamMagieListView,
    WarhamMontureListView,
    WarhamPlayerDetailView,
    WarhamInventaireListView,
    WarhamMontureCreateView,
    WarhamPlayerCreateView,
    WarhamCampaignCreateView,
    WarhamArmeContactCreateView,
    WarhamArmeDistanceCreateView,
    WarhamArmureCreateView,
    WarhamCompetenceCreateView,
    WarhamEquipementCreateView,
    WarhamPlanCarriereCreateView,
    WarhamBourseCreateView,
    WarhamMontureCreateView,
    WarhamMagieCreateView,
    WarhamSortilegeCreateView,
    WarhamArmeContactUpdateView,
    WarhamArmeDistanceUpdateView,
    WarhamMontureUpdateView,
    WarhamArmureUpdateView,
    WarhamCompetenceUpdateView,
    WarhamEquipementUpdateView,
    WarhamExperienceUpdateView,
    WarhamPlayerCampagneUpdate,
    WarhamBourseUpdateView,
    WarhamPlanCarriereUpdateView,
    WarhamCaracteristiqueActuelleUpdateView,
    WarhamCampagneUpdateView,
    WarhamDetailsDescriptionPersonnageUpdateView,
    WarhamMagieUpdateView,
    WarhamSortilegeUpdateView,
    WarhamArmeDistanceDeleteViews,
    WarhamCampagneDeleteViews,
    WarhamPlayerDeleteViews,
    WarhamArmeContactDeleteViews,
    WarhamArmureDeleteViews,
    WarhamCompetenceDeleteViews,
    WarhamEquipementDeleteViews,
    WarhamBourseDeleteViews,
    WarhamPointBlessureUpdateView,
    WarhamPointDestinUpdateView,
    WarhamMontureDeleteViews,
)


app_name = "warhammer"

urlpatterns = [
    #### camapgne url ####
    path("", WarhamCampaignListView.as_view(), name="liste_campagne"),
    path(
        "Creationcampagne/",
        WarhamCampaignCreateView.as_view(),
        name="creation_campagne",
    ),
    path(
        "edit_campagne/<int:pk>/",
        WarhamCampagneUpdateView.as_view(),
        name="editter_campagne",
    ),
    path(
        "campagne_delete/<int:pk>/",
        WarhamCampagneDeleteViews.as_view(),
        name="supprimer_campagne",
    ),
    path(
        "campagne/<int:pk>/",
        WarhamCampaignPlayerListView.as_view(),
        name="liste_personnages",
    ),
    #### player url ####
    path(
        "creationplayer/",
        WarhamPlayerCreateView.as_view(),
        name="creation_personnage",
    ),
    path(
        "player/<int:pk>/",
        WarhamPlayerDetailView.as_view(),
        name="details_personnages",
    ),
    path(
        "Edit_personnage/<int:pk>/",
        WarhamDetailsDescriptionPersonnageUpdateView.as_view(),
        name="editter_personnage",
    ),
    path(
        "player_delete/<int:pk>/",
        WarhamPlayerDeleteViews.as_view(),
        name="supprimer_personnages",
    ),
    path(
        "AjouteCampagne/<int:pk>/",
        WarhamPlayerCampagneUpdate.as_view(),
        name="ajouter_campagne",
    ),  #### Arme Contact url ####
    path(
        "<int:pk>/AjouterArmeContact/",
        WarhamArmeContactCreateView.as_view(),
        name="ajouter_armeContact",
    ),
    path(
        "Edit_armeContact/<int:pk>/",
        WarhamArmeContactUpdateView.as_view(),
        name="editter_armeContact",
    ),
    path(
        "delete_armeContact/<int:pk>/",
        WarhamArmeContactDeleteViews.as_view(),
        name="supprimer_armeContact",
    ),  #### Arme Distance url ####
    path(
        "<int:pk>/AjouterArmeDistance/",
        WarhamArmeDistanceCreateView.as_view(),
        name="ajouter_armeDistance",
    ),
    path(
        "Edit_armeDistance/<int:pk>/",
        WarhamArmeDistanceUpdateView.as_view(),
        name="editter_armeDistance",
    ),
    path(
        "delete_armeDistance/<int:pk>/",
        WarhamArmeDistanceDeleteViews.as_view(),
        name="supprimer_armeDistance",
    ),  #### Armure url ####
    path(
        "<int:pk>/AjouterArmure/",
        WarhamArmureCreateView.as_view(),
        name="ajouter_armure",
    ),
    path(
        "Edit_armure/<int:pk>/",
        WarhamArmureUpdateView.as_view(),
        name="editter_armure",
    ),
    path(
        "delete_armure/<int:pk>/",
        WarhamArmureDeleteViews.as_view(),
        name="supprimer_armure",
    ),  #### Competence url ####
    path(
        "<int:pk>/AjouterCompetence/",
        WarhamCompetenceCreateView.as_view(),
        name="ajouter_competence",
    ),
    path(
        "Edit_competence/<int:pk>/",
        WarhamCompetenceUpdateView.as_view(),
        name="editter_competence",
    ),
    path(
        "delete_competence/<int:pk>/",
        WarhamCompetenceDeleteViews.as_view(),
        name="supprimer_competence",
    ),  #### Equipements url ####
    path(
        "<int:pk>/AjouterEquipement/",
        WarhamEquipementCreateView.as_view(),
        name="ajouter_equipement",
    ),
    path(
        "Edit_equipement/<int:pk>/",
        WarhamEquipementUpdateView.as_view(),
        name="editter_equipement",
    ),
    path(
        "delete_equipement/<int:pk>/",
        WarhamEquipementDeleteViews.as_view(),
        name="supprimer_equipement",
    ),  #### Bourse url ####
    path(
        "<int:pk>/AjouterBourse/",
        WarhamBourseCreateView.as_view(),
        name="ajouter_bourse",
    ),
    path(
        "Edit_bourse/<int:pk>/",
        WarhamBourseUpdateView.as_view(),
        name="editter_bourse",
    ),
    path(
        "delete_bourse/<int:pk>/",
        WarhamBourseDeleteViews.as_view(),
        name="supprimer_bourse",
    ),  #### Carriere url ####
    path(
        "<int:pk>/AjouterCarriere/",
        WarhamPlanCarriereCreateView.as_view(),
        name="ajouter_carriere",
    ),
    path(
        "Edit_carriere/<int:pk>/",
        WarhamPlanCarriereUpdateView.as_view(),
        name="editter_carriere",
    ),
    path(
        "Edit_carriere_actuelle/<int:pk>/",
        WarhamCaracteristiqueActuelleUpdateView.as_view(),
        name="editter_carriere_actuelle",
    ),  #### Experience url ####
    path(
        "Edit_experience/<int:pk>/",
        WarhamExperienceUpdateView.as_view(),
        name="editter_experience",
    ),  #### Points de blessure url ####
    path(
        "Edit_blessure/<int:pk>/",
        WarhamPointBlessureUpdateView.as_view(),
        name="editter_blessure",
    ),  #### Points de destin url ####
    path(
        "Edit_destin/<int:pk>/",
        WarhamPointDestinUpdateView.as_view(),
        name="editter_destin",
    ),  #### Monture url ####
    path(
        "monture/<int:pk>/",
        WarhamMontureListView.as_view(),
        name="details_monture",
    ),
    path(
        "<int:pk>/AjouterMonture/",
        WarhamMontureCreateView.as_view(),
        name="ajouter_monture",
    ),
    path(
        "Edit_monture/<int:pk>/",
        WarhamMontureUpdateView.as_view(),
        name="editter_monture",
    ),
    path(
        "delete_monture/<int:pk>/",
        WarhamMontureDeleteViews.as_view(),
        name="supprimer_monture",
    ),  #### Magie url ####
    path(
        "magie/<int:pk>/",
        WarhamMagieListView.as_view(),
        name="details_magie",
    ),
    path(
        "<int:pk>/AjouterMagie/",
        WarhamMagieCreateView.as_view(),
        name="ajouter_magie",
    ),
    path(
        "Edit_magie/<int:pk>/",
        WarhamMagieUpdateView.as_view(),
        name="editter_magie",
    ),  #### Sortilege url ####
    path(
        "<int:pk>/AjouterSort/",
        WarhamSortilegeCreateView.as_view(),
        name="ajouter_sortilege",
    ),
    path(
        "Edit_sort/<int:pk>/",
        WarhamSortilegeUpdateView.as_view(),
        name="editter_sortilege",
    ),  #### Inventaire url ####
    path(
        "inventaire/<int:pk>/",
        WarhamInventaireListView.as_view(),
        name="details_inventaire",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
