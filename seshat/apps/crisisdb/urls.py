from .models import Agricultural_population, Arable_land, Arable_land_per_farmer, Gross_grain_shared_per_agricultural_population, Net_grain_shared_per_agricultural_population, Surplus, Military_expense, Silver_inflow, Silver_stock, Total_population, Gdp_per_capita, Drought_event, Locust_event, Socioeconomic_turmoil_event, Crop_failure_event, Famine_event, Disease_outbreak
from django.urls import path

from . import views

urlpatterns = [
    path('vars/', views.QingVars, name='qing_vars'),
    path('playground/', views.playground, name='playground'),
]


urlpatterns += [
    path('agricultural_population/create/', views.Agricultural_populationCreate.as_view(),
         name="agricultural_population-create"),

    path('agricultural_populations/', views.Agricultural_populationListView.as_view(), name='agricultural_populations'),
    path('agricultural_population/<int:pk>', views.Agricultural_populationDetailView.as_view(),
         name='agricultural_population-detail'),
    path('agricultural_population/<int:pk>/update/',
         views.Agricultural_populationUpdate.as_view(), name="agricultural_population-update"),
    path('agricultural_population/<int:pk>/delete/',
         views.Agricultural_populationDelete.as_view(), name="agricultural_population-delete"),
    # Download
    path('agricultural_populationdownload/', views.agricultural_population_download,
         name="agricultural_population-download"),
]
        

urlpatterns += [
    path('arable_land/create/', views.Arable_landCreate.as_view(),
         name="arable_land-create"),

    path('arable_lands/', views.Arable_landListView.as_view(), name='arable_lands'),
    path('arable_land/<int:pk>', views.Arable_landDetailView.as_view(),
         name='arable_land-detail'),
    path('arable_land/<int:pk>/update/',
         views.Arable_landUpdate.as_view(), name="arable_land-update"),
    path('arable_land/<int:pk>/delete/',
         views.Arable_landDelete.as_view(), name="arable_land-delete"),
    # Download
    path('arable_landdownload/', views.arable_land_download,
         name="arable_land-download"),
]
        

urlpatterns += [
    path('arable_land_per_farmer/create/', views.Arable_land_per_farmerCreate.as_view(),
         name="arable_land_per_farmer-create"),

    path('arable_land_per_farmers/', views.Arable_land_per_farmerListView.as_view(), name='arable_land_per_farmers'),
    path('arable_land_per_farmer/<int:pk>', views.Arable_land_per_farmerDetailView.as_view(),
         name='arable_land_per_farmer-detail'),
    path('arable_land_per_farmer/<int:pk>/update/',
         views.Arable_land_per_farmerUpdate.as_view(), name="arable_land_per_farmer-update"),
    path('arable_land_per_farmer/<int:pk>/delete/',
         views.Arable_land_per_farmerDelete.as_view(), name="arable_land_per_farmer-delete"),
    # Download
    path('arable_land_per_farmerdownload/', views.arable_land_per_farmer_download,
         name="arable_land_per_farmer-download"),
]
        

urlpatterns += [
    path('gross_grain_shared_per_agricultural_population/create/', views.Gross_grain_shared_per_agricultural_populationCreate.as_view(),
         name="gross_grain_shared_per_agricultural_population-create"),

    path('gross_grain_shared_per_agricultural_populations/', views.Gross_grain_shared_per_agricultural_populationListView.as_view(), name='gross_grain_shared_per_agricultural_populations'),
    path('gross_grain_shared_per_agricultural_population/<int:pk>', views.Gross_grain_shared_per_agricultural_populationDetailView.as_view(),
         name='gross_grain_shared_per_agricultural_population-detail'),
    path('gross_grain_shared_per_agricultural_population/<int:pk>/update/',
         views.Gross_grain_shared_per_agricultural_populationUpdate.as_view(), name="gross_grain_shared_per_agricultural_population-update"),
    path('gross_grain_shared_per_agricultural_population/<int:pk>/delete/',
         views.Gross_grain_shared_per_agricultural_populationDelete.as_view(), name="gross_grain_shared_per_agricultural_population-delete"),
    # Download
    path('gross_grain_shared_per_agricultural_populationdownload/', views.gross_grain_shared_per_agricultural_population_download,
         name="gross_grain_shared_per_agricultural_population-download"),
]
        

urlpatterns += [
    path('net_grain_shared_per_agricultural_population/create/', views.Net_grain_shared_per_agricultural_populationCreate.as_view(),
         name="net_grain_shared_per_agricultural_population-create"),

    path('net_grain_shared_per_agricultural_populations/', views.Net_grain_shared_per_agricultural_populationListView.as_view(), name='net_grain_shared_per_agricultural_populations'),
    path('net_grain_shared_per_agricultural_population/<int:pk>', views.Net_grain_shared_per_agricultural_populationDetailView.as_view(),
         name='net_grain_shared_per_agricultural_population-detail'),
    path('net_grain_shared_per_agricultural_population/<int:pk>/update/',
         views.Net_grain_shared_per_agricultural_populationUpdate.as_view(), name="net_grain_shared_per_agricultural_population-update"),
    path('net_grain_shared_per_agricultural_population/<int:pk>/delete/',
         views.Net_grain_shared_per_agricultural_populationDelete.as_view(), name="net_grain_shared_per_agricultural_population-delete"),
    # Download
    path('net_grain_shared_per_agricultural_populationdownload/', views.net_grain_shared_per_agricultural_population_download,
         name="net_grain_shared_per_agricultural_population-download"),
]
        

urlpatterns += [
    path('surplus/create/', views.SurplusCreate.as_view(),
         name="surplus-create"),

    path('surplus/', views.SurplusListView.as_view(), name='surplus'),
    path('surplus/<int:pk>', views.SurplusDetailView.as_view(),
         name='surplus-detail'),
    path('surplus/<int:pk>/update/',
         views.SurplusUpdate.as_view(), name="surplus-update"),
    path('surplus/<int:pk>/delete/',
         views.SurplusDelete.as_view(), name="surplus-delete"),
    # Download
    path('surplusdownload/', views.surplus_download,
         name="surplus-download"),
]
        

urlpatterns += [
    path('military_expense/create/', views.Military_expenseCreate.as_view(),
         name="military_expense-create"),

    path('military_expenses/', views.Military_expenseListView.as_view(), name='military_expenses'),
    path('military_expense/<int:pk>', views.Military_expenseDetailView.as_view(),
         name='military_expense-detail'),
    path('military_expense/<int:pk>/update/',
         views.Military_expenseUpdate.as_view(), name="military_expense-update"),
    path('military_expense/<int:pk>/delete/',
         views.Military_expenseDelete.as_view(), name="military_expense-delete"),
    # Download
    path('military_expensedownload/', views.military_expense_download,
         name="military_expense-download"),
]
        

urlpatterns += [
    path('silver_inflow/create/', views.Silver_inflowCreate.as_view(),
         name="silver_inflow-create"),

    path('silver_inflows/', views.Silver_inflowListView.as_view(), name='silver_inflows'),
    path('silver_inflow/<int:pk>', views.Silver_inflowDetailView.as_view(),
         name='silver_inflow-detail'),
    path('silver_inflow/<int:pk>/update/',
         views.Silver_inflowUpdate.as_view(), name="silver_inflow-update"),
    path('silver_inflow/<int:pk>/delete/',
         views.Silver_inflowDelete.as_view(), name="silver_inflow-delete"),
    # Download
    path('silver_inflowdownload/', views.silver_inflow_download,
         name="silver_inflow-download"),
]
        

urlpatterns += [
    path('silver_stock/create/', views.Silver_stockCreate.as_view(),
         name="silver_stock-create"),

    path('silver_stocks/', views.Silver_stockListView.as_view(), name='silver_stocks'),
    path('silver_stock/<int:pk>', views.Silver_stockDetailView.as_view(),
         name='silver_stock-detail'),
    path('silver_stock/<int:pk>/update/',
         views.Silver_stockUpdate.as_view(), name="silver_stock-update"),
    path('silver_stock/<int:pk>/delete/',
         views.Silver_stockDelete.as_view(), name="silver_stock-delete"),
    # Download
    path('silver_stockdownload/', views.silver_stock_download,
         name="silver_stock-download"),
]
        

urlpatterns += [
    path('total_population/create/', views.Total_populationCreate.as_view(),
         name="total_population-create"),

    path('total_populations/', views.Total_populationListView.as_view(), name='total_populations'),
    path('total_population/<int:pk>', views.Total_populationDetailView.as_view(),
         name='total_population-detail'),
    path('total_population/<int:pk>/update/',
         views.Total_populationUpdate.as_view(), name="total_population-update"),
    path('total_population/<int:pk>/delete/',
         views.Total_populationDelete.as_view(), name="total_population-delete"),
    # Download
    path('total_populationdownload/', views.total_population_download,
         name="total_population-download"),
]
        

urlpatterns += [
    path('gdp_per_capita/create/', views.Gdp_per_capitaCreate.as_view(),
         name="gdp_per_capita-create"),

    path('gdp_per_capitas/', views.Gdp_per_capitaListView.as_view(), name='gdp_per_capitas'),
    path('gdp_per_capita/<int:pk>', views.Gdp_per_capitaDetailView.as_view(),
         name='gdp_per_capita-detail'),
    path('gdp_per_capita/<int:pk>/update/',
         views.Gdp_per_capitaUpdate.as_view(), name="gdp_per_capita-update"),
    path('gdp_per_capita/<int:pk>/delete/',
         views.Gdp_per_capitaDelete.as_view(), name="gdp_per_capita-delete"),
    # Download
    path('gdp_per_capitadownload/', views.gdp_per_capita_download,
         name="gdp_per_capita-download"),
]
        

urlpatterns += [
    path('drought_event/create/', views.Drought_eventCreate.as_view(),
         name="drought_event-create"),

    path('drought_events/', views.Drought_eventListView.as_view(), name='drought_events'),
    path('drought_event/<int:pk>', views.Drought_eventDetailView.as_view(),
         name='drought_event-detail'),
    path('drought_event/<int:pk>/update/',
         views.Drought_eventUpdate.as_view(), name="drought_event-update"),
    path('drought_event/<int:pk>/delete/',
         views.Drought_eventDelete.as_view(), name="drought_event-delete"),
    # Download
    path('drought_eventdownload/', views.drought_event_download,
         name="drought_event-download"),
]
        

urlpatterns += [
    path('locust_event/create/', views.Locust_eventCreate.as_view(),
         name="locust_event-create"),

    path('locust_events/', views.Locust_eventListView.as_view(), name='locust_events'),
    path('locust_event/<int:pk>', views.Locust_eventDetailView.as_view(),
         name='locust_event-detail'),
    path('locust_event/<int:pk>/update/',
         views.Locust_eventUpdate.as_view(), name="locust_event-update"),
    path('locust_event/<int:pk>/delete/',
         views.Locust_eventDelete.as_view(), name="locust_event-delete"),
    # Download
    path('locust_eventdownload/', views.locust_event_download,
         name="locust_event-download"),
]
        

urlpatterns += [
    path('socioeconomic_turmoil_event/create/', views.Socioeconomic_turmoil_eventCreate.as_view(),
         name="socioeconomic_turmoil_event-create"),

    path('socioeconomic_turmoil_events/', views.Socioeconomic_turmoil_eventListView.as_view(), name='socioeconomic_turmoil_events'),
    path('socioeconomic_turmoil_event/<int:pk>', views.Socioeconomic_turmoil_eventDetailView.as_view(),
         name='socioeconomic_turmoil_event-detail'),
    path('socioeconomic_turmoil_event/<int:pk>/update/',
         views.Socioeconomic_turmoil_eventUpdate.as_view(), name="socioeconomic_turmoil_event-update"),
    path('socioeconomic_turmoil_event/<int:pk>/delete/',
         views.Socioeconomic_turmoil_eventDelete.as_view(), name="socioeconomic_turmoil_event-delete"),
    # Download
    path('socioeconomic_turmoil_eventdownload/', views.socioeconomic_turmoil_event_download,
         name="socioeconomic_turmoil_event-download"),
]
        

urlpatterns += [
    path('crop_failure_event/create/', views.Crop_failure_eventCreate.as_view(),
         name="crop_failure_event-create"),

    path('crop_failure_events/', views.Crop_failure_eventListView.as_view(), name='crop_failure_events'),
    path('crop_failure_event/<int:pk>', views.Crop_failure_eventDetailView.as_view(),
         name='crop_failure_event-detail'),
    path('crop_failure_event/<int:pk>/update/',
         views.Crop_failure_eventUpdate.as_view(), name="crop_failure_event-update"),
    path('crop_failure_event/<int:pk>/delete/',
         views.Crop_failure_eventDelete.as_view(), name="crop_failure_event-delete"),
    # Download
    path('crop_failure_eventdownload/', views.crop_failure_event_download,
         name="crop_failure_event-download"),
]
        

urlpatterns += [
    path('famine_event/create/', views.Famine_eventCreate.as_view(),
         name="famine_event-create"),

    path('famine_events/', views.Famine_eventListView.as_view(), name='famine_events'),
    path('famine_event/<int:pk>', views.Famine_eventDetailView.as_view(),
         name='famine_event-detail'),
    path('famine_event/<int:pk>/update/',
         views.Famine_eventUpdate.as_view(), name="famine_event-update"),
    path('famine_event/<int:pk>/delete/',
         views.Famine_eventDelete.as_view(), name="famine_event-delete"),
    # Download
    path('famine_eventdownload/', views.famine_event_download,
         name="famine_event-download"),
]
        

urlpatterns += [
    path('disease_outbreak/create/', views.Disease_outbreakCreate.as_view(),
         name="disease_outbreak-create"),

    path('disease_outbreaks/', views.Disease_outbreakListView.as_view(), name='disease_outbreaks'),
    path('disease_outbreak/<int:pk>', views.Disease_outbreakDetailView.as_view(),
         name='disease_outbreak-detail'),
    path('disease_outbreak/<int:pk>/update/',
         views.Disease_outbreakUpdate.as_view(), name="disease_outbreak-update"),
    path('disease_outbreak/<int:pk>/delete/',
         views.Disease_outbreakDelete.as_view(), name="disease_outbreak-delete"),
    # Download
    path('disease_outbreakdownload/', views.disease_outbreak_download,
         name="disease_outbreak-download"),
]
        