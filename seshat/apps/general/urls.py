from .models import Polity_research_assistant, Polity_utm_zone, Polity_original_name, Polity_alternative_name, Polity_peak_years, Polity_duration, Polity_degree_of_centralization, Polity_suprapolity_relations, Polity_capital, Polity_language, Polity_linguistic_family, Polity_language_genus, Polity_religion_genus, Polity_religion_family, Polity_religion, Polity_relationship_to_preceding_entity, Polity_preceding_entity, Polity_succeeding_entity, Polity_supracultural_entity, Polity_scale_of_supracultural_interaction, Polity_alternate_religion_genus, Polity_alternate_religion_family, Polity_alternate_religion, Polity_expert, Polity_editor, Polity_religious_tradition
from django.urls import path

from . import views

urlpatterns = [
    path('generalvars/', views.generalvars, name='generalvars'),
]


urlpatterns += [
    path('polity_research_assistant/create/', views.Polity_research_assistantCreate.as_view(),
         name="polity_research_assistant-create"),

    path('polity_research_assistants/', views.Polity_research_assistantListView.as_view(), name='polity_research_assistants'),
    path('polity_research_assistants_all/', views.Polity_research_assistantListViewAll.as_view(), name='polity_research_assistants_all'),
    path('polity_research_assistant/<int:pk>', views.Polity_research_assistantDetailView.as_view(),
         name='polity_research_assistant-detail'),
    path('polity_research_assistant/<int:pk>/update/',
         views.Polity_research_assistantUpdate.as_view(), name="polity_research_assistant-update"),
    path('polity_research_assistant/<int:pk>/delete/',
         views.Polity_research_assistantDelete.as_view(), name="polity_research_assistant-delete"),
    # Download
    path('polity_research_assistantdownload/', views.polity_research_assistant_download,
         name="polity_research_assistant-download"),
    path('polity_research_assistantmetadownload/', views.polity_research_assistant_meta_download,
         name="polity_research_assistant-metadownload"),
]
        

urlpatterns += [
    path('polity_utm_zone/create/', views.Polity_utm_zoneCreate.as_view(),
         name="polity_utm_zone-create"),

    path('polity_utm_zones/', views.Polity_utm_zoneListView.as_view(), name='polity_utm_zones'),
    path('polity_utm_zones_all/', views.Polity_utm_zoneListViewAll.as_view(), name='polity_utm_zones_all'),
    path('polity_utm_zone/<int:pk>', views.Polity_utm_zoneDetailView.as_view(),
         name='polity_utm_zone-detail'),
    path('polity_utm_zone/<int:pk>/update/',
         views.Polity_utm_zoneUpdate.as_view(), name="polity_utm_zone-update"),
    path('polity_utm_zone/<int:pk>/delete/',
         views.Polity_utm_zoneDelete.as_view(), name="polity_utm_zone-delete"),
    # Download
    path('polity_utm_zonedownload/', views.polity_utm_zone_download,
         name="polity_utm_zone-download"),
    path('polity_utm_zonemetadownload/', views.polity_utm_zone_meta_download,
         name="polity_utm_zone-metadownload"),
]
        

urlpatterns += [
    path('polity_original_name/create/', views.Polity_original_nameCreate.as_view(),
         name="polity_original_name-create"),

    path('polity_original_names/', views.Polity_original_nameListView.as_view(), name='polity_original_names'),
    path('polity_original_names_all/', views.Polity_original_nameListViewAll.as_view(), name='polity_original_names_all'),
    path('polity_original_name/<int:pk>', views.Polity_original_nameDetailView.as_view(),
         name='polity_original_name-detail'),
    path('polity_original_name/<int:pk>/update/',
         views.Polity_original_nameUpdate.as_view(), name="polity_original_name-update"),
    path('polity_original_name/<int:pk>/delete/',
         views.Polity_original_nameDelete.as_view(), name="polity_original_name-delete"),
    # Download
    path('polity_original_namedownload/', views.polity_original_name_download,
         name="polity_original_name-download"),
    path('polity_original_namemetadownload/', views.polity_original_name_meta_download,
         name="polity_original_name-metadownload"),
]
        

urlpatterns += [
    path('polity_alternative_name/create/', views.Polity_alternative_nameCreate.as_view(),
         name="polity_alternative_name-create"),

    path('polity_alternative_names/', views.Polity_alternative_nameListView.as_view(), name='polity_alternative_names'),
    path('polity_alternative_names_all/', views.Polity_alternative_nameListViewAll.as_view(), name='polity_alternative_names_all'),
    path('polity_alternative_name/<int:pk>', views.Polity_alternative_nameDetailView.as_view(),
         name='polity_alternative_name-detail'),
    path('polity_alternative_name/<int:pk>/update/',
         views.Polity_alternative_nameUpdate.as_view(), name="polity_alternative_name-update"),
    path('polity_alternative_name/<int:pk>/delete/',
         views.Polity_alternative_nameDelete.as_view(), name="polity_alternative_name-delete"),
    # Download
    path('polity_alternative_namedownload/', views.polity_alternative_name_download,
         name="polity_alternative_name-download"),
    path('polity_alternative_namemetadownload/', views.polity_alternative_name_meta_download,
         name="polity_alternative_name-metadownload"),
]
        

urlpatterns += [
    path('polity_peak_years/create/', views.Polity_peak_yearsCreate.as_view(),
         name="polity_peak_years-create"),

    path('polity_peak_yearss/', views.Polity_peak_yearsListView.as_view(), name='polity_peak_yearss'),
    path('polity_peak_yearss_all/', views.Polity_peak_yearsListViewAll.as_view(), name='polity_peak_yearss_all'),
    path('polity_peak_years/<int:pk>', views.Polity_peak_yearsDetailView.as_view(),
         name='polity_peak_years-detail'),
    path('polity_peak_years/<int:pk>/update/',
         views.Polity_peak_yearsUpdate.as_view(), name="polity_peak_years-update"),
    path('polity_peak_years/<int:pk>/delete/',
         views.Polity_peak_yearsDelete.as_view(), name="polity_peak_years-delete"),
    # Download
    path('polity_peak_yearsdownload/', views.polity_peak_years_download,
         name="polity_peak_years-download"),
    path('polity_peak_yearsmetadownload/', views.polity_peak_years_meta_download,
         name="polity_peak_years-metadownload"),
]
        

urlpatterns += [
    path('polity_duration/create/', views.Polity_durationCreate.as_view(),
         name="polity_duration-create"),

    path('polity_durations/', views.Polity_durationListView.as_view(), name='polity_durations'),
    path('polity_durations_all/', views.Polity_durationListViewAll.as_view(), name='polity_durations_all'),
    path('polity_duration/<int:pk>', views.Polity_durationDetailView.as_view(),
         name='polity_duration-detail'),
    path('polity_duration/<int:pk>/update/',
         views.Polity_durationUpdate.as_view(), name="polity_duration-update"),
    path('polity_duration/<int:pk>/delete/',
         views.Polity_durationDelete.as_view(), name="polity_duration-delete"),
    # Download
    path('polity_durationdownload/', views.polity_duration_download,
         name="polity_duration-download"),
    path('polity_durationmetadownload/', views.polity_duration_meta_download,
         name="polity_duration-metadownload"),
]
        

urlpatterns += [
    path('polity_degree_of_centralization/create/', views.Polity_degree_of_centralizationCreate.as_view(),
         name="polity_degree_of_centralization-create"),

    path('polity_degree_of_centralizations/', views.Polity_degree_of_centralizationListView.as_view(), name='polity_degree_of_centralizations'),
    path('polity_degree_of_centralizations_all/', views.Polity_degree_of_centralizationListViewAll.as_view(), name='polity_degree_of_centralizations_all'),
    path('polity_degree_of_centralization/<int:pk>', views.Polity_degree_of_centralizationDetailView.as_view(),
         name='polity_degree_of_centralization-detail'),
    path('polity_degree_of_centralization/<int:pk>/update/',
         views.Polity_degree_of_centralizationUpdate.as_view(), name="polity_degree_of_centralization-update"),
    path('polity_degree_of_centralization/<int:pk>/delete/',
         views.Polity_degree_of_centralizationDelete.as_view(), name="polity_degree_of_centralization-delete"),
    # Download
    path('polity_degree_of_centralizationdownload/', views.polity_degree_of_centralization_download,
         name="polity_degree_of_centralization-download"),
    path('polity_degree_of_centralizationmetadownload/', views.polity_degree_of_centralization_meta_download,
         name="polity_degree_of_centralization-metadownload"),
]
        

urlpatterns += [
    path('polity_suprapolity_relations/create/', views.Polity_suprapolity_relationsCreate.as_view(),
         name="polity_suprapolity_relations-create"),

    path('polity_suprapolity_relationss/', views.Polity_suprapolity_relationsListView.as_view(), name='polity_suprapolity_relationss'),
    path('polity_suprapolity_relationss_all/', views.Polity_suprapolity_relationsListViewAll.as_view(), name='polity_suprapolity_relationss_all'),
    path('polity_suprapolity_relations/<int:pk>', views.Polity_suprapolity_relationsDetailView.as_view(),
         name='polity_suprapolity_relations-detail'),
    path('polity_suprapolity_relations/<int:pk>/update/',
         views.Polity_suprapolity_relationsUpdate.as_view(), name="polity_suprapolity_relations-update"),
    path('polity_suprapolity_relations/<int:pk>/delete/',
         views.Polity_suprapolity_relationsDelete.as_view(), name="polity_suprapolity_relations-delete"),
    # Download
    path('polity_suprapolity_relationsdownload/', views.polity_suprapolity_relations_download,
         name="polity_suprapolity_relations-download"),
    path('polity_suprapolity_relationsmetadownload/', views.polity_suprapolity_relations_meta_download,
         name="polity_suprapolity_relations-metadownload"),
]
        

urlpatterns += [
    path('polity_capital/create/', views.Polity_capitalCreate.as_view(),
         name="polity_capital-create"),

    path('polity_capitals/', views.Polity_capitalListView.as_view(), name='polity_capitals'),
    path('polity_capitals_all/', views.Polity_capitalListViewAll.as_view(), name='polity_capitals_all'),
    path('polity_capital/<int:pk>', views.Polity_capitalDetailView.as_view(),
         name='polity_capital-detail'),
    path('polity_capital/<int:pk>/update/',
         views.Polity_capitalUpdate.as_view(), name="polity_capital-update"),
    path('polity_capital/<int:pk>/delete/',
         views.Polity_capitalDelete.as_view(), name="polity_capital-delete"),
    # Download
    path('polity_capitaldownload/', views.polity_capital_download,
         name="polity_capital-download"),
    path('polity_capitalmetadownload/', views.polity_capital_meta_download,
         name="polity_capital-metadownload"),
]
        

urlpatterns += [
    path('polity_language/create/', views.Polity_languageCreate.as_view(),
         name="polity_language-create"),

    path('polity_languages/', views.Polity_languageListView.as_view(), name='polity_languages'),
    path('polity_languages_all/', views.Polity_languageListViewAll.as_view(), name='polity_languages_all'),
    path('polity_language/<int:pk>', views.Polity_languageDetailView.as_view(),
         name='polity_language-detail'),
    path('polity_language/<int:pk>/update/',
         views.Polity_languageUpdate.as_view(), name="polity_language-update"),
    path('polity_language/<int:pk>/delete/',
         views.Polity_languageDelete.as_view(), name="polity_language-delete"),
    # Download
    path('polity_languagedownload/', views.polity_language_download,
         name="polity_language-download"),
    path('polity_languagemetadownload/', views.polity_language_meta_download,
         name="polity_language-metadownload"),
]
        

urlpatterns += [
    path('polity_linguistic_family/create/', views.Polity_linguistic_familyCreate.as_view(),
         name="polity_linguistic_family-create"),

    path('polity_linguistic_familys/', views.Polity_linguistic_familyListView.as_view(), name='polity_linguistic_familys'),
    path('polity_linguistic_familys_all/', views.Polity_linguistic_familyListViewAll.as_view(), name='polity_linguistic_familys_all'),
    path('polity_linguistic_family/<int:pk>', views.Polity_linguistic_familyDetailView.as_view(),
         name='polity_linguistic_family-detail'),
    path('polity_linguistic_family/<int:pk>/update/',
         views.Polity_linguistic_familyUpdate.as_view(), name="polity_linguistic_family-update"),
    path('polity_linguistic_family/<int:pk>/delete/',
         views.Polity_linguistic_familyDelete.as_view(), name="polity_linguistic_family-delete"),
    # Download
    path('polity_linguistic_familydownload/', views.polity_linguistic_family_download,
         name="polity_linguistic_family-download"),
    path('polity_linguistic_familymetadownload/', views.polity_linguistic_family_meta_download,
         name="polity_linguistic_family-metadownload"),
]
        

urlpatterns += [
    path('polity_language_genus/create/', views.Polity_language_genusCreate.as_view(),
         name="polity_language_genus-create"),

    path('polity_language_genuss/', views.Polity_language_genusListView.as_view(), name='polity_language_genuss'),
    path('polity_language_genuss_all/', views.Polity_language_genusListViewAll.as_view(), name='polity_language_genuss_all'),
    path('polity_language_genus/<int:pk>', views.Polity_language_genusDetailView.as_view(),
         name='polity_language_genus-detail'),
    path('polity_language_genus/<int:pk>/update/',
         views.Polity_language_genusUpdate.as_view(), name="polity_language_genus-update"),
    path('polity_language_genus/<int:pk>/delete/',
         views.Polity_language_genusDelete.as_view(), name="polity_language_genus-delete"),
    # Download
    path('polity_language_genusdownload/', views.polity_language_genus_download,
         name="polity_language_genus-download"),
    path('polity_language_genusmetadownload/', views.polity_language_genus_meta_download,
         name="polity_language_genus-metadownload"),
]
        

urlpatterns += [
    path('polity_religion_genus/create/', views.Polity_religion_genusCreate.as_view(),
         name="polity_religion_genus-create"),

    path('polity_religion_genuss/', views.Polity_religion_genusListView.as_view(), name='polity_religion_genuss'),
    path('polity_religion_genuss_all/', views.Polity_religion_genusListViewAll.as_view(), name='polity_religion_genuss_all'),
    path('polity_religion_genus/<int:pk>', views.Polity_religion_genusDetailView.as_view(),
         name='polity_religion_genus-detail'),
    path('polity_religion_genus/<int:pk>/update/',
         views.Polity_religion_genusUpdate.as_view(), name="polity_religion_genus-update"),
    path('polity_religion_genus/<int:pk>/delete/',
         views.Polity_religion_genusDelete.as_view(), name="polity_religion_genus-delete"),
    # Download
    path('polity_religion_genusdownload/', views.polity_religion_genus_download,
         name="polity_religion_genus-download"),
    path('polity_religion_genusmetadownload/', views.polity_religion_genus_meta_download,
         name="polity_religion_genus-metadownload"),
]
        

urlpatterns += [
    path('polity_religion_family/create/', views.Polity_religion_familyCreate.as_view(),
         name="polity_religion_family-create"),

    path('polity_religion_familys/', views.Polity_religion_familyListView.as_view(), name='polity_religion_familys'),
    path('polity_religion_familys_all/', views.Polity_religion_familyListViewAll.as_view(), name='polity_religion_familys_all'),
    path('polity_religion_family/<int:pk>', views.Polity_religion_familyDetailView.as_view(),
         name='polity_religion_family-detail'),
    path('polity_religion_family/<int:pk>/update/',
         views.Polity_religion_familyUpdate.as_view(), name="polity_religion_family-update"),
    path('polity_religion_family/<int:pk>/delete/',
         views.Polity_religion_familyDelete.as_view(), name="polity_religion_family-delete"),
    # Download
    path('polity_religion_familydownload/', views.polity_religion_family_download,
         name="polity_religion_family-download"),
    path('polity_religion_familymetadownload/', views.polity_religion_family_meta_download,
         name="polity_religion_family-metadownload"),
]
        

urlpatterns += [
    path('polity_religion/create/', views.Polity_religionCreate.as_view(),
         name="polity_religion-create"),

    path('polity_religions/', views.Polity_religionListView.as_view(), name='polity_religions'),
    path('polity_religions_all/', views.Polity_religionListViewAll.as_view(), name='polity_religions_all'),
    path('polity_religion/<int:pk>', views.Polity_religionDetailView.as_view(),
         name='polity_religion-detail'),
    path('polity_religion/<int:pk>/update/',
         views.Polity_religionUpdate.as_view(), name="polity_religion-update"),
    path('polity_religion/<int:pk>/delete/',
         views.Polity_religionDelete.as_view(), name="polity_religion-delete"),
    # Download
    path('polity_religiondownload/', views.polity_religion_download,
         name="polity_religion-download"),
    path('polity_religionmetadownload/', views.polity_religion_meta_download,
         name="polity_religion-metadownload"),
]
        

urlpatterns += [
    path('polity_relationship_to_preceding_entity/create/', views.Polity_relationship_to_preceding_entityCreate.as_view(),
         name="polity_relationship_to_preceding_entity-create"),

    path('polity_relationship_to_preceding_entitys/', views.Polity_relationship_to_preceding_entityListView.as_view(), name='polity_relationship_to_preceding_entitys'),
    path('polity_relationship_to_preceding_entitys_all/', views.Polity_relationship_to_preceding_entityListViewAll.as_view(), name='polity_relationship_to_preceding_entitys_all'),
    path('polity_relationship_to_preceding_entity/<int:pk>', views.Polity_relationship_to_preceding_entityDetailView.as_view(),
         name='polity_relationship_to_preceding_entity-detail'),
    path('polity_relationship_to_preceding_entity/<int:pk>/update/',
         views.Polity_relationship_to_preceding_entityUpdate.as_view(), name="polity_relationship_to_preceding_entity-update"),
    path('polity_relationship_to_preceding_entity/<int:pk>/delete/',
         views.Polity_relationship_to_preceding_entityDelete.as_view(), name="polity_relationship_to_preceding_entity-delete"),
    # Download
    path('polity_relationship_to_preceding_entitydownload/', views.polity_relationship_to_preceding_entity_download,
         name="polity_relationship_to_preceding_entity-download"),
    path('polity_relationship_to_preceding_entitymetadownload/', views.polity_relationship_to_preceding_entity_meta_download,
         name="polity_relationship_to_preceding_entity-metadownload"),
]
        

urlpatterns += [
    path('polity_preceding_entity/create/', views.Polity_preceding_entityCreate.as_view(),
         name="polity_preceding_entity-create"),

    path('polity_preceding_entitys/', views.Polity_preceding_entityListView.as_view(), name='polity_preceding_entitys'),
    path('polity_preceding_entitys_all/', views.Polity_preceding_entityListViewAll.as_view(), name='polity_preceding_entitys_all'),
    path('polity_preceding_entity/<int:pk>', views.Polity_preceding_entityDetailView.as_view(),
         name='polity_preceding_entity-detail'),
    path('polity_preceding_entity/<int:pk>/update/',
         views.Polity_preceding_entityUpdate.as_view(), name="polity_preceding_entity-update"),
    path('polity_preceding_entity/<int:pk>/delete/',
         views.Polity_preceding_entityDelete.as_view(), name="polity_preceding_entity-delete"),
    # Download
    path('polity_preceding_entitydownload/', views.polity_preceding_entity_download,
         name="polity_preceding_entity-download"),
    path('polity_preceding_entitymetadownload/', views.polity_preceding_entity_meta_download,
         name="polity_preceding_entity-metadownload"),
]
        

urlpatterns += [
    path('polity_succeeding_entity/create/', views.Polity_succeeding_entityCreate.as_view(),
         name="polity_succeeding_entity-create"),

    path('polity_succeeding_entitys/', views.Polity_succeeding_entityListView.as_view(), name='polity_succeeding_entitys'),
    path('polity_succeeding_entitys_all/', views.Polity_succeeding_entityListViewAll.as_view(), name='polity_succeeding_entitys_all'),
    path('polity_succeeding_entity/<int:pk>', views.Polity_succeeding_entityDetailView.as_view(),
         name='polity_succeeding_entity-detail'),
    path('polity_succeeding_entity/<int:pk>/update/',
         views.Polity_succeeding_entityUpdate.as_view(), name="polity_succeeding_entity-update"),
    path('polity_succeeding_entity/<int:pk>/delete/',
         views.Polity_succeeding_entityDelete.as_view(), name="polity_succeeding_entity-delete"),
    # Download
    path('polity_succeeding_entitydownload/', views.polity_succeeding_entity_download,
         name="polity_succeeding_entity-download"),
    path('polity_succeeding_entitymetadownload/', views.polity_succeeding_entity_meta_download,
         name="polity_succeeding_entity-metadownload"),
]
        

urlpatterns += [
    path('polity_supracultural_entity/create/', views.Polity_supracultural_entityCreate.as_view(),
         name="polity_supracultural_entity-create"),

    path('polity_supracultural_entitys/', views.Polity_supracultural_entityListView.as_view(), name='polity_supracultural_entitys'),
    path('polity_supracultural_entitys_all/', views.Polity_supracultural_entityListViewAll.as_view(), name='polity_supracultural_entitys_all'),
    path('polity_supracultural_entity/<int:pk>', views.Polity_supracultural_entityDetailView.as_view(),
         name='polity_supracultural_entity-detail'),
    path('polity_supracultural_entity/<int:pk>/update/',
         views.Polity_supracultural_entityUpdate.as_view(), name="polity_supracultural_entity-update"),
    path('polity_supracultural_entity/<int:pk>/delete/',
         views.Polity_supracultural_entityDelete.as_view(), name="polity_supracultural_entity-delete"),
    # Download
    path('polity_supracultural_entitydownload/', views.polity_supracultural_entity_download,
         name="polity_supracultural_entity-download"),
    path('polity_supracultural_entitymetadownload/', views.polity_supracultural_entity_meta_download,
         name="polity_supracultural_entity-metadownload"),
]
        

urlpatterns += [
    path('polity_scale_of_supracultural_interaction/create/', views.Polity_scale_of_supracultural_interactionCreate.as_view(),
         name="polity_scale_of_supracultural_interaction-create"),

    path('polity_scale_of_supracultural_interactions/', views.Polity_scale_of_supracultural_interactionListView.as_view(), name='polity_scale_of_supracultural_interactions'),
    path('polity_scale_of_supracultural_interactions_all/', views.Polity_scale_of_supracultural_interactionListViewAll.as_view(), name='polity_scale_of_supracultural_interactions_all'),
    path('polity_scale_of_supracultural_interaction/<int:pk>', views.Polity_scale_of_supracultural_interactionDetailView.as_view(),
         name='polity_scale_of_supracultural_interaction-detail'),
    path('polity_scale_of_supracultural_interaction/<int:pk>/update/',
         views.Polity_scale_of_supracultural_interactionUpdate.as_view(), name="polity_scale_of_supracultural_interaction-update"),
    path('polity_scale_of_supracultural_interaction/<int:pk>/delete/',
         views.Polity_scale_of_supracultural_interactionDelete.as_view(), name="polity_scale_of_supracultural_interaction-delete"),
    # Download
    path('polity_scale_of_supracultural_interactiondownload/', views.polity_scale_of_supracultural_interaction_download,
         name="polity_scale_of_supracultural_interaction-download"),
    path('polity_scale_of_supracultural_interactionmetadownload/', views.polity_scale_of_supracultural_interaction_meta_download,
         name="polity_scale_of_supracultural_interaction-metadownload"),
]
        

urlpatterns += [
    path('polity_alternate_religion_genus/create/', views.Polity_alternate_religion_genusCreate.as_view(),
         name="polity_alternate_religion_genus-create"),

    path('polity_alternate_religion_genuss/', views.Polity_alternate_religion_genusListView.as_view(), name='polity_alternate_religion_genuss'),
    path('polity_alternate_religion_genuss_all/', views.Polity_alternate_religion_genusListViewAll.as_view(), name='polity_alternate_religion_genuss_all'),
    path('polity_alternate_religion_genus/<int:pk>', views.Polity_alternate_religion_genusDetailView.as_view(),
         name='polity_alternate_religion_genus-detail'),
    path('polity_alternate_religion_genus/<int:pk>/update/',
         views.Polity_alternate_religion_genusUpdate.as_view(), name="polity_alternate_religion_genus-update"),
    path('polity_alternate_religion_genus/<int:pk>/delete/',
         views.Polity_alternate_religion_genusDelete.as_view(), name="polity_alternate_religion_genus-delete"),
    # Download
    path('polity_alternate_religion_genusdownload/', views.polity_alternate_religion_genus_download,
         name="polity_alternate_religion_genus-download"),
    path('polity_alternate_religion_genusmetadownload/', views.polity_alternate_religion_genus_meta_download,
         name="polity_alternate_religion_genus-metadownload"),
]
        

urlpatterns += [
    path('polity_alternate_religion_family/create/', views.Polity_alternate_religion_familyCreate.as_view(),
         name="polity_alternate_religion_family-create"),

    path('polity_alternate_religion_familys/', views.Polity_alternate_religion_familyListView.as_view(), name='polity_alternate_religion_familys'),
    path('polity_alternate_religion_familys_all/', views.Polity_alternate_religion_familyListViewAll.as_view(), name='polity_alternate_religion_familys_all'),
    path('polity_alternate_religion_family/<int:pk>', views.Polity_alternate_religion_familyDetailView.as_view(),
         name='polity_alternate_religion_family-detail'),
    path('polity_alternate_religion_family/<int:pk>/update/',
         views.Polity_alternate_religion_familyUpdate.as_view(), name="polity_alternate_religion_family-update"),
    path('polity_alternate_religion_family/<int:pk>/delete/',
         views.Polity_alternate_religion_familyDelete.as_view(), name="polity_alternate_religion_family-delete"),
    # Download
    path('polity_alternate_religion_familydownload/', views.polity_alternate_religion_family_download,
         name="polity_alternate_religion_family-download"),
    path('polity_alternate_religion_familymetadownload/', views.polity_alternate_religion_family_meta_download,
         name="polity_alternate_religion_family-metadownload"),
]
        

urlpatterns += [
    path('polity_alternate_religion/create/', views.Polity_alternate_religionCreate.as_view(),
         name="polity_alternate_religion-create"),

    path('polity_alternate_religions/', views.Polity_alternate_religionListView.as_view(), name='polity_alternate_religions'),
    path('polity_alternate_religions_all/', views.Polity_alternate_religionListViewAll.as_view(), name='polity_alternate_religions_all'),
    path('polity_alternate_religion/<int:pk>', views.Polity_alternate_religionDetailView.as_view(),
         name='polity_alternate_religion-detail'),
    path('polity_alternate_religion/<int:pk>/update/',
         views.Polity_alternate_religionUpdate.as_view(), name="polity_alternate_religion-update"),
    path('polity_alternate_religion/<int:pk>/delete/',
         views.Polity_alternate_religionDelete.as_view(), name="polity_alternate_religion-delete"),
    # Download
    path('polity_alternate_religiondownload/', views.polity_alternate_religion_download,
         name="polity_alternate_religion-download"),
    path('polity_alternate_religionmetadownload/', views.polity_alternate_religion_meta_download,
         name="polity_alternate_religion-metadownload"),
]
        

urlpatterns += [
    path('polity_expert/create/', views.Polity_expertCreate.as_view(),
         name="polity_expert-create"),

    path('polity_experts/', views.Polity_expertListView.as_view(), name='polity_experts'),
    path('polity_experts_all/', views.Polity_expertListViewAll.as_view(), name='polity_experts_all'),
    path('polity_expert/<int:pk>', views.Polity_expertDetailView.as_view(),
         name='polity_expert-detail'),
    path('polity_expert/<int:pk>/update/',
         views.Polity_expertUpdate.as_view(), name="polity_expert-update"),
    path('polity_expert/<int:pk>/delete/',
         views.Polity_expertDelete.as_view(), name="polity_expert-delete"),
    # Download
    path('polity_expertdownload/', views.polity_expert_download,
         name="polity_expert-download"),
    path('polity_expertmetadownload/', views.polity_expert_meta_download,
         name="polity_expert-metadownload"),
]
        

urlpatterns += [
    path('polity_editor/create/', views.Polity_editorCreate.as_view(),
         name="polity_editor-create"),

    path('polity_editors/', views.Polity_editorListView.as_view(), name='polity_editors'),
    path('polity_editors_all/', views.Polity_editorListViewAll.as_view(), name='polity_editors_all'),
    path('polity_editor/<int:pk>', views.Polity_editorDetailView.as_view(),
         name='polity_editor-detail'),
    path('polity_editor/<int:pk>/update/',
         views.Polity_editorUpdate.as_view(), name="polity_editor-update"),
    path('polity_editor/<int:pk>/delete/',
         views.Polity_editorDelete.as_view(), name="polity_editor-delete"),
    # Download
    path('polity_editordownload/', views.polity_editor_download,
         name="polity_editor-download"),
    path('polity_editormetadownload/', views.polity_editor_meta_download,
         name="polity_editor-metadownload"),
]
        

urlpatterns += [
    path('polity_religious_tradition/create/', views.Polity_religious_traditionCreate.as_view(),
         name="polity_religious_tradition-create"),

    path('polity_religious_traditions/', views.Polity_religious_traditionListView.as_view(), name='polity_religious_traditions'),
    path('polity_religious_traditions_all/', views.Polity_religious_traditionListViewAll.as_view(), name='polity_religious_traditions_all'),
    path('polity_religious_tradition/<int:pk>', views.Polity_religious_traditionDetailView.as_view(),
         name='polity_religious_tradition-detail'),
    path('polity_religious_tradition/<int:pk>/update/',
         views.Polity_religious_traditionUpdate.as_view(), name="polity_religious_tradition-update"),
    path('polity_religious_tradition/<int:pk>/delete/',
         views.Polity_religious_traditionDelete.as_view(), name="polity_religious_tradition-delete"),
    # Download
    path('polity_religious_traditiondownload/', views.polity_religious_tradition_download,
         name="polity_religious_tradition-download"),
    path('polity_religious_traditionmetadownload/', views.polity_religious_tradition_meta_download,
         name="polity_religious_tradition-metadownload"),
]
        