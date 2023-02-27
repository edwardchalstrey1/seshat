
from seshat.utils.utils import adder, dic_of_all_vars, list_of_all_Polities, dic_of_all_vars_in_sections, dic_of_all_vars_with_varhier
from django.db.models.base import Model
# from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.safestring import mark_safe
from django.views.generic.list import ListView

from django.contrib.contenttypes.models import ContentType

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponseRedirect, response, JsonResponse
from ..core.models import Citation, Reference, Polity, Section, Subsection, Country, Variablehierarchy

# from .mycodes import *
from django.conf import settings

from django.urls import reverse, reverse_lazy

from django.views import generic
import csv
import datetime

from django.core.paginator import Paginator

from django.http import HttpResponse

import requests
from requests.structures import CaseInsensitiveDict



from .models import Ra, Polity_territory, Polity_population, Population_of_the_largest_settlement, Settlement_hierarchy, Administrative_level, Religious_level, Military_level, Professional_military_officer, Professional_soldier, Professional_priesthood, Full_time_bureaucrat, Examination_system, Merit_promotion, Specialized_government_building, Formal_legal_code, Judge, Court, Professional_lawyer, Irrigation_system, Drinking_water_supply_system, Market, Food_storage_site, Road, Bridge, Canal, Port, Mines_or_quarry, Mnemonic_device, Nonwritten_record, Written_record, Script, Non_phonetic_writing, Phonetic_alphabetic_writing, Lists_tables_and_classification, Calendar, Sacred_text, Religious_literature, Practical_literature, History, Philosophy, Scientific_literature, Fiction, Article, Token, Precious_metal, Foreign_coin, Indigenous_coin, Paper_currency, Courier, Postal_station, General_postal_service


from .forms import RaForm, Polity_territoryForm, Polity_populationForm, Population_of_the_largest_settlementForm, Settlement_hierarchyForm, Administrative_levelForm, Religious_levelForm, Military_levelForm, Professional_military_officerForm, Professional_soldierForm, Professional_priesthoodForm, Full_time_bureaucratForm, Examination_systemForm, Merit_promotionForm, Specialized_government_buildingForm, Formal_legal_codeForm, JudgeForm, CourtForm, Professional_lawyerForm, Irrigation_systemForm, Drinking_water_supply_systemForm, MarketForm, Food_storage_siteForm, RoadForm, BridgeForm, CanalForm, PortForm, Mines_or_quarryForm, Mnemonic_deviceForm, Nonwritten_recordForm, Written_recordForm, ScriptForm, Non_phonetic_writingForm, Phonetic_alphabetic_writingForm, Lists_tables_and_classificationForm, CalendarForm, Sacred_textForm, Religious_literatureForm, Practical_literatureForm, HistoryForm, PhilosophyForm, Scientific_literatureForm, FictionForm, ArticleForm, TokenForm, Precious_metalForm, Foreign_coinForm, Indigenous_coinForm, Paper_currencyForm, CourierForm, Postal_stationForm, General_postal_serviceForm

class RaCreate(PermissionRequiredMixin, CreateView):
    model = Ra
    form_class = RaForm
    template_name = "sc/ra/ra_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('ra-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "ra"
        context["my_exp"] = "The name of the research assistant or associate who coded the data. If more than one RA made a substantial contribution, list all via separate entries."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'sc_ra': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The RA of Social Complexity Variables', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class RaUpdate(PermissionRequiredMixin, UpdateView):
    model = Ra
    form_class = RaForm
    template_name = "sc/ra/ra_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "ra"

        return context

class RaDelete(PermissionRequiredMixin, DeleteView):
    model = Ra
    success_url = reverse_lazy('ras')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class RaListView(generic.ListView):
    model = Ra
    template_name = "sc/ra/ra_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('ras')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "ra"
        context["var_main_desc"] = "The name of the research assistant or associate who coded the data. if more than one ra made a substantial contribution, list all via separate entries."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "staff"
        context["inner_vars"] = {'sc_ra': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The RA of Social Complexity Variables', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class RaListViewAll(generic.ListView):
    model = Ra
    template_name = "sc/ra/ra_list_all.html"

    def get_absolute_url(self):
        return reverse('ras_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Ra.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "ra"
        context["var_main_desc"] = "The name of the research assistant or associate who coded the data. if more than one ra made a substantial contribution, list all via separate entries."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "staff"
        context["inner_vars"] = {'sc_ra': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The RA of Social Complexity Variables', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class RaDetailView(generic.DetailView):
    model = Ra
    template_name = "sc/ra/ra_detail.html"


@permission_required('admin.can_add_log_entry')
def ra_download(request):
    items = Ra.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ras.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'sc_ra', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.sc_ra, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def ra_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ras.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'The name of the research assistant or associate who coded the data. If more than one RA made a substantial contribution, list all via separate entries.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'staff'}
    my_meta_data_dic_inner_vars = {'sc_ra': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The RA of Social Complexity Variables', 'units': None, 'choices': None, 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_territoryCreate(PermissionRequiredMixin, CreateView):
    model = Polity_territory
    form_class = Polity_territoryForm
    template_name = "sc/polity_territory/polity_territory_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('polity_territory-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Territory"
        context["my_exp"] = "Talking about Social Scale, Polity territory is coded in squared kilometers."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'polity_territory_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of polity territory for a polity.', 'units': 'km squared', 'choices': None, 'null_meaning': None}, 'polity_territory_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of polity territory for a polity.', 'units': 'km squared', 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Polity_territoryUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_territory
    form_class = Polity_territoryForm
    template_name = "sc/polity_territory/polity_territory_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Territory"

        return context

class Polity_territoryDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_territory
    success_url = reverse_lazy('polity_territorys')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Polity_territoryListView(generic.ListView):
    model = Polity_territory
    template_name = "sc/polity_territory/polity_territory_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_territorys')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Territory"
        context["var_main_desc"] = "Talking about social scale, polity territory is coded in squared kilometers."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Social Scale"
        context["inner_vars"] = {'polity_territory_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of polity territory for a polity.', 'units': 'km squared', 'choices': None, 'null_meaning': None}, 'polity_territory_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of polity territory for a polity.', 'units': 'km squared', 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = ['Units']

        return context


class Polity_territoryListViewAll(generic.ListView):
    model = Polity_territory
    template_name = "sc/polity_territory/polity_territory_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_territorys_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_territory.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Territory"
        context["var_main_desc"] = "Talking about social scale, polity territory is coded in squared kilometers."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Social Scale"
        context["inner_vars"] = {'polity_territory_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of polity territory for a polity.', 'units': 'km squared', 'choices': None, 'null_meaning': None}, 'polity_territory_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of polity territory for a polity.', 'units': 'km squared', 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = ['Units']
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_territoryDetailView(generic.DetailView):
    model = Polity_territory
    template_name = "sc/polity_territory/polity_territory_detail.html"


@permission_required('admin.can_add_log_entry')
def polity_territory_download(request):
    items = Polity_territory.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_territorys.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'polity_territory_from', 'polity_territory_to', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.polity_territory_from, obj.polity_territory_to, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def polity_territory_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_territorys.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Social Scale, Polity territory is coded in squared kilometers.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Social Scale'}
    my_meta_data_dic_inner_vars = {'polity_territory_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of polity territory for a polity.', 'units': 'km squared', 'choices': None, 'null_meaning': None}, 'polity_territory_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of polity territory for a polity.', 'units': 'km squared', 'choices': None, 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_populationCreate(PermissionRequiredMixin, CreateView):
    model = Polity_population
    form_class = Polity_populationForm
    template_name = "sc/polity_population/polity_population_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('polity_population-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Population"
        context["my_exp"] = "Talking about Social Scale, Polity Population is the estimated population of the polity; can change as a result of both adding/losing new territories or by population growth/decline within a region"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'polity_population_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of polity population for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'polity_population_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of polity population for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Polity_populationUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_population
    form_class = Polity_populationForm
    template_name = "sc/polity_population/polity_population_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Population"

        return context

class Polity_populationDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_population
    success_url = reverse_lazy('polity_populations')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Polity_populationListView(generic.ListView):
    model = Polity_population
    template_name = "sc/polity_population/polity_population_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_populations')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Population"
        context["var_main_desc"] = "Talking about social scale, polity population is the estimated population of the polity; can change as a result of both adding/losing new territories or by population growth/decline within a region"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Social Scale"
        context["inner_vars"] = {'polity_population_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of polity population for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'polity_population_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of polity population for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Polity_populationListViewAll(generic.ListView):
    model = Polity_population
    template_name = "sc/polity_population/polity_population_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_populations_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_population.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Population"
        context["var_main_desc"] = "Talking about social scale, polity population is the estimated population of the polity; can change as a result of both adding/losing new territories or by population growth/decline within a region"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Social Scale"
        context["inner_vars"] = {'polity_population_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of polity population for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'polity_population_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of polity population for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_populationDetailView(generic.DetailView):
    model = Polity_population
    template_name = "sc/polity_population/polity_population_detail.html"


@permission_required('admin.can_add_log_entry')
def polity_population_download(request):
    items = Polity_population.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_populations.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'polity_population_from', 'polity_population_to', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.polity_population_from, obj.polity_population_to, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def polity_population_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_populations.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Social Scale, Polity Population is the estimated population of the polity; can change as a result of both adding/losing new territories or by population growth/decline within a region', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Social Scale'}
    my_meta_data_dic_inner_vars = {'polity_population_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of polity population for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'polity_population_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of polity population for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Population_of_the_largest_settlementCreate(PermissionRequiredMixin, CreateView):
    model = Population_of_the_largest_settlement
    form_class = Population_of_the_largest_settlementForm
    template_name = "sc/population_of_the_largest_settlement/population_of_the_largest_settlement_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('population_of_the_largest_settlement-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Population of the Largest Settlement"
        context["my_exp"] = "Talking about Social Scale, Population of the largest settlement is the estimated population of the largest settlement of the polity. Note that the largest settlement could be different from the capital (coded under General Variables). If possible, indicate the dynamics (that is, how population changed during the temporal period of the polity). Note that we are also building a city database - you should consult it as it may already have the needed data."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'population_of_the_largest_settlement_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of population of the largest settlement for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'population_of_the_largest_settlement_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of population of the largest settlement for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Population_of_the_largest_settlementUpdate(PermissionRequiredMixin, UpdateView):
    model = Population_of_the_largest_settlement
    form_class = Population_of_the_largest_settlementForm
    template_name = "sc/population_of_the_largest_settlement/population_of_the_largest_settlement_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Population of the Largest Settlement"

        return context

class Population_of_the_largest_settlementDelete(PermissionRequiredMixin, DeleteView):
    model = Population_of_the_largest_settlement
    success_url = reverse_lazy('population_of_the_largest_settlements')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Population_of_the_largest_settlementListView(generic.ListView):
    model = Population_of_the_largest_settlement
    template_name = "sc/population_of_the_largest_settlement/population_of_the_largest_settlement_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('population_of_the_largest_settlements')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Population of the Largest Settlement"
        context["var_main_desc"] = "Talking about social scale, population of the largest settlement is the estimated population of the largest settlement of the polity. note that the largest settlement could be different from the capital (coded under general variables). if possible, indicate the dynamics (that is, how population changed during the temporal period of the polity). note that we are also building a city database - you should consult it as it may already have the needed data."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Social Scale"
        context["inner_vars"] = {'population_of_the_largest_settlement_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of population of the largest settlement for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'population_of_the_largest_settlement_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of population of the largest settlement for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Population_of_the_largest_settlementListViewAll(generic.ListView):
    model = Population_of_the_largest_settlement
    template_name = "sc/population_of_the_largest_settlement/population_of_the_largest_settlement_list_all.html"

    def get_absolute_url(self):
        return reverse('population_of_the_largest_settlements_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Population_of_the_largest_settlement.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Population of the Largest Settlement"
        context["var_main_desc"] = "Talking about social scale, population of the largest settlement is the estimated population of the largest settlement of the polity. note that the largest settlement could be different from the capital (coded under general variables). if possible, indicate the dynamics (that is, how population changed during the temporal period of the polity). note that we are also building a city database - you should consult it as it may already have the needed data."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Social Scale"
        context["inner_vars"] = {'population_of_the_largest_settlement_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of population of the largest settlement for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'population_of_the_largest_settlement_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of population of the largest settlement for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Population_of_the_largest_settlementDetailView(generic.DetailView):
    model = Population_of_the_largest_settlement
    template_name = "sc/population_of_the_largest_settlement/population_of_the_largest_settlement_detail.html"


@permission_required('admin.can_add_log_entry')
def population_of_the_largest_settlement_download(request):
    items = Population_of_the_largest_settlement.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="population_of_the_largest_settlements.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'population_of_the_largest_settlement_from', 'population_of_the_largest_settlement_to', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.population_of_the_largest_settlement_from, obj.population_of_the_largest_settlement_to, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def population_of_the_largest_settlement_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="population_of_the_largest_settlements.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Social Scale, Population of the largest settlement is the estimated population of the largest settlement of the polity. Note that the largest settlement could be different from the capital (coded under General Variables). If possible, indicate the dynamics (that is, how population changed during the temporal period of the polity). Note that we are also building a city database - you should consult it as it may already have the needed data.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Social Scale'}
    my_meta_data_dic_inner_vars = {'population_of_the_largest_settlement_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of population of the largest settlement for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'population_of_the_largest_settlement_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of population of the largest settlement for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Settlement_hierarchyCreate(PermissionRequiredMixin, CreateView):
    model = Settlement_hierarchy
    form_class = Settlement_hierarchyForm
    template_name = "sc/settlement_hierarchy/settlement_hierarchy_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('settlement_hierarchy-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Settlement Hierarchy"
        context["my_exp"] = "Talking about Hierarchical Complexity, Settlement hierarchy records (in levels) the hierarchy of not just settlement sizes, but also their complexity as reflected in different roles they play within the (quasi)polity. As settlements become more populous they acquire more complex functions: transportational (e.g. port); economic (e.g. market); administrative (e.g. storehouse, local government building); cultural (e.g. theatre); religious (e.g. temple), utilitarian (e.g. hospital), monumental (e.g. statues, plazas). Example: (1) Large City (monumental structures, theatre, market, hospital, central government buildings) (2) City (market, theatre, regional government buildings) (3) Large Town (market, administrative buildings) (4) Town (administrative buildings, storehouse)) (5) Village (shrine) (6) Hamlet (residential only). In the narrative paragraph explain the different levels and list their functions. Provide a (crude) estimate of population sizes. For example, Large Town (market, temple, administrative buildings): 2,000-5,000 inhabitants."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'settlement_hierarchy_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of settlement hierarchy for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'settlement_hierarchy_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of settlement hierarchy for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Settlement_hierarchyUpdate(PermissionRequiredMixin, UpdateView):
    model = Settlement_hierarchy
    form_class = Settlement_hierarchyForm
    template_name = "sc/settlement_hierarchy/settlement_hierarchy_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Settlement Hierarchy"

        return context

class Settlement_hierarchyDelete(PermissionRequiredMixin, DeleteView):
    model = Settlement_hierarchy
    success_url = reverse_lazy('settlement_hierarchys')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Settlement_hierarchyListView(generic.ListView):
    model = Settlement_hierarchy
    template_name = "sc/settlement_hierarchy/settlement_hierarchy_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('settlement_hierarchys')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Settlement Hierarchy"
        context["var_main_desc"] = "Talking about hierarchical complexity, settlement hierarchy records (in levels) the hierarchy of not just settlement sizes, but also their complexity as reflected in different roles they play within the (quasi)polity. as settlements become more populous they acquire more complex functions: transportational (e.g. port); economic (e.g. market); administrative (e.g. storehouse, local government building); cultural (e.g. theatre); religious (e.g. temple), utilitarian (e.g. hospital), monumental (e.g. statues, plazas). example: (1) large city (monumental structures, theatre, market, hospital, central government buildings) (2) city (market, theatre, regional government buildings) (3) large town (market, administrative buildings) (4) town (administrative buildings, storehouse)) (5) village (shrine) (6) hamlet (residential only). in the narrative paragraph explain the different levels and list their functions. provide a (crude) estimate of population sizes. for example, large town (market, temple, administrative buildings): 2,000-5,000 inhabitants."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Hierarchical Complexity"
        context["inner_vars"] = {'settlement_hierarchy_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of settlement hierarchy for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'settlement_hierarchy_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of settlement hierarchy for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Settlement_hierarchyListViewAll(generic.ListView):
    model = Settlement_hierarchy
    template_name = "sc/settlement_hierarchy/settlement_hierarchy_list_all.html"

    def get_absolute_url(self):
        return reverse('settlement_hierarchys_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Settlement_hierarchy.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Settlement Hierarchy"
        context["var_main_desc"] = "Talking about hierarchical complexity, settlement hierarchy records (in levels) the hierarchy of not just settlement sizes, but also their complexity as reflected in different roles they play within the (quasi)polity. as settlements become more populous they acquire more complex functions: transportational (e.g. port); economic (e.g. market); administrative (e.g. storehouse, local government building); cultural (e.g. theatre); religious (e.g. temple), utilitarian (e.g. hospital), monumental (e.g. statues, plazas). example: (1) large city (monumental structures, theatre, market, hospital, central government buildings) (2) city (market, theatre, regional government buildings) (3) large town (market, administrative buildings) (4) town (administrative buildings, storehouse)) (5) village (shrine) (6) hamlet (residential only). in the narrative paragraph explain the different levels and list their functions. provide a (crude) estimate of population sizes. for example, large town (market, temple, administrative buildings): 2,000-5,000 inhabitants."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Hierarchical Complexity"
        context["inner_vars"] = {'settlement_hierarchy_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of settlement hierarchy for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'settlement_hierarchy_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of settlement hierarchy for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Settlement_hierarchyDetailView(generic.DetailView):
    model = Settlement_hierarchy
    template_name = "sc/settlement_hierarchy/settlement_hierarchy_detail.html"


@permission_required('admin.can_add_log_entry')
def settlement_hierarchy_download(request):
    items = Settlement_hierarchy.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="settlement_hierarchys.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'settlement_hierarchy_from', 'settlement_hierarchy_to', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.settlement_hierarchy_from, obj.settlement_hierarchy_to, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def settlement_hierarchy_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="settlement_hierarchys.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Hierarchical Complexity, Settlement hierarchy records (in levels) the hierarchy of not just settlement sizes, but also their complexity as reflected in different roles they play within the (quasi)polity. As settlements become more populous they acquire more complex functions: transportational (e.g. port); economic (e.g. market); administrative (e.g. storehouse, local government building); cultural (e.g. theatre); religious (e.g. temple), utilitarian (e.g. hospital), monumental (e.g. statues, plazas). Example: (1) Large City (monumental structures, theatre, market, hospital, central government buildings) (2) City (market, theatre, regional government buildings) (3) Large Town (market, administrative buildings) (4) Town (administrative buildings, storehouse)) (5) Village (shrine) (6) Hamlet (residential only). In the narrative paragraph explain the different levels and list their functions. Provide a (crude) estimate of population sizes. For example, Large Town (market, temple, administrative buildings): 2,000-5,000 inhabitants.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Hierarchical Complexity'}
    my_meta_data_dic_inner_vars = {'settlement_hierarchy_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of settlement hierarchy for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'settlement_hierarchy_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of settlement hierarchy for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Administrative_levelCreate(PermissionRequiredMixin, CreateView):
    model = Administrative_level
    form_class = Administrative_levelForm
    template_name = "sc/administrative_level/administrative_level_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('administrative_level-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Administrative Level"
        context["my_exp"] = "Talking about Hierarchical Complexity, Administrative levels records the administrative levels of a polity. An example of hierarchy for a state society could be (1) the overall ruler, (2) provincial/regional governors, (3) district heads, (4) town mayors, (5) village heads. Note that unlike in settlement hierarchy, here you code people hierarchy. Do not simply copy settlement hierarchy data here. For archaeological polities, you will usually code as 'unknown', unless experts identified ranks of chiefs or officials independently of the settlement hierarchy. Note: Often there are more than one concurrent administrative hierarchy. In the example above the hierarchy refers to the territorial government. In addition, the ruler may have a hierarchically organized central bureaucracy located in the capital. For example, (4)the overall ruler, (3) chiefs of various ministries, (2) midlevel bureaucrats, (1) scribes and clerks. In the narrative paragraph detail what is known about both hierarchies. The machine-readable code should reflect the largest number (the longer chain of command)."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'administrative_level_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of administrative level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'administrative_level_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of administrative level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Administrative_levelUpdate(PermissionRequiredMixin, UpdateView):
    model = Administrative_level
    form_class = Administrative_levelForm
    template_name = "sc/administrative_level/administrative_level_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Administrative Level"

        return context

class Administrative_levelDelete(PermissionRequiredMixin, DeleteView):
    model = Administrative_level
    success_url = reverse_lazy('administrative_levels')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Administrative_levelListView(generic.ListView):
    model = Administrative_level
    template_name = "sc/administrative_level/administrative_level_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('administrative_levels')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Administrative Level"
        context["var_main_desc"] = "Talking about hierarchical complexity, administrative levels records the administrative levels of a polity. an example of hierarchy for a state society could be (1) the overall ruler, (2) provincial/regional governors, (3) district heads, (4) town mayors, (5) village heads. note that unlike in settlement hierarchy, here you code people hierarchy. do not simply copy settlement hierarchy data here. for archaeological polities, you will usually code as 'unknown', unless experts identified ranks of chiefs or officials independently of the settlement hierarchy. note: often there are more than one concurrent administrative hierarchy. in the example above the hierarchy refers to the territorial government. in addition, the ruler may have a hierarchically organized central bureaucracy located in the capital. for example, (4)the overall ruler, (3) chiefs of various ministries, (2) midlevel bureaucrats, (1) scribes and clerks. in the narrative paragraph detail what is known about both hierarchies. the machine-readable code should reflect the largest number (the longer chain of command)."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Hierarchical Complexity"
        context["inner_vars"] = {'administrative_level_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of administrative level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'administrative_level_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of administrative level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Administrative_levelListViewAll(generic.ListView):
    model = Administrative_level
    template_name = "sc/administrative_level/administrative_level_list_all.html"

    def get_absolute_url(self):
        return reverse('administrative_levels_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Administrative_level.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Administrative Level"
        context["var_main_desc"] = "Talking about hierarchical complexity, administrative levels records the administrative levels of a polity. an example of hierarchy for a state society could be (1) the overall ruler, (2) provincial/regional governors, (3) district heads, (4) town mayors, (5) village heads. note that unlike in settlement hierarchy, here you code people hierarchy. do not simply copy settlement hierarchy data here. for archaeological polities, you will usually code as 'unknown', unless experts identified ranks of chiefs or officials independently of the settlement hierarchy. note: often there are more than one concurrent administrative hierarchy. in the example above the hierarchy refers to the territorial government. in addition, the ruler may have a hierarchically organized central bureaucracy located in the capital. for example, (4)the overall ruler, (3) chiefs of various ministries, (2) midlevel bureaucrats, (1) scribes and clerks. in the narrative paragraph detail what is known about both hierarchies. the machine-readable code should reflect the largest number (the longer chain of command)."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Hierarchical Complexity"
        context["inner_vars"] = {'administrative_level_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of administrative level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'administrative_level_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of administrative level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Administrative_levelDetailView(generic.DetailView):
    model = Administrative_level
    template_name = "sc/administrative_level/administrative_level_detail.html"


@permission_required('admin.can_add_log_entry')
def administrative_level_download(request):
    items = Administrative_level.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="administrative_levels.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'administrative_level_from', 'administrative_level_to', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.administrative_level_from, obj.administrative_level_to, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def administrative_level_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="administrative_levels.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': "Talking about Hierarchical Complexity, Administrative levels records the administrative levels of a polity. An example of hierarchy for a state society could be (1) the overall ruler, (2) provincial/regional governors, (3) district heads, (4) town mayors, (5) village heads. Note that unlike in settlement hierarchy, here you code people hierarchy. Do not simply copy settlement hierarchy data here. For archaeological polities, you will usually code as 'unknown', unless experts identified ranks of chiefs or officials independently of the settlement hierarchy. Note: Often there are more than one concurrent administrative hierarchy. In the example above the hierarchy refers to the territorial government. In addition, the ruler may have a hierarchically organized central bureaucracy located in the capital. For example, (4)the overall ruler, (3) chiefs of various ministries, (2) midlevel bureaucrats, (1) scribes and clerks. In the narrative paragraph detail what is known about both hierarchies. The machine-readable code should reflect the largest number (the longer chain of command).", 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Hierarchical Complexity'}
    my_meta_data_dic_inner_vars = {'administrative_level_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of administrative level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'administrative_level_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of administrative level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Religious_levelCreate(PermissionRequiredMixin, CreateView):
    model = Religious_level
    form_class = Religious_levelForm
    template_name = "sc/religious_level/religious_level_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('religious_level-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Religious Level"
        context["my_exp"] = "Talking about Hierarchical Complexity, Religious levels records the Religious levels of a polity. Same principle as with Administrative levels. Start with the head of the official cult (if present) coded as: level 1, and work down to the local priest."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'religious_level_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of religious level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'religious_level_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of religious level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Religious_levelUpdate(PermissionRequiredMixin, UpdateView):
    model = Religious_level
    form_class = Religious_levelForm
    template_name = "sc/religious_level/religious_level_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Religious Level"

        return context

class Religious_levelDelete(PermissionRequiredMixin, DeleteView):
    model = Religious_level
    success_url = reverse_lazy('religious_levels')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Religious_levelListView(generic.ListView):
    model = Religious_level
    template_name = "sc/religious_level/religious_level_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('religious_levels')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Religious Level"
        context["var_main_desc"] = "Talking about hierarchical complexity, religious levels records the religious levels of a polity. same principle as with administrative levels. start with the head of the official cult (if present) coded as: level 1, and work down to the local priest."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Hierarchical Complexity"
        context["inner_vars"] = {'religious_level_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of religious level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'religious_level_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of religious level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Religious_levelListViewAll(generic.ListView):
    model = Religious_level
    template_name = "sc/religious_level/religious_level_list_all.html"

    def get_absolute_url(self):
        return reverse('religious_levels_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Religious_level.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Religious Level"
        context["var_main_desc"] = "Talking about hierarchical complexity, religious levels records the religious levels of a polity. same principle as with administrative levels. start with the head of the official cult (if present) coded as: level 1, and work down to the local priest."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Hierarchical Complexity"
        context["inner_vars"] = {'religious_level_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of religious level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'religious_level_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of religious level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Religious_levelDetailView(generic.DetailView):
    model = Religious_level
    template_name = "sc/religious_level/religious_level_detail.html"


@permission_required('admin.can_add_log_entry')
def religious_level_download(request):
    items = Religious_level.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="religious_levels.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'religious_level_from', 'religious_level_to', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.religious_level_from, obj.religious_level_to, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def religious_level_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="religious_levels.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Hierarchical Complexity, Religious levels records the Religious levels of a polity. Same principle as with Administrative levels. Start with the head of the official cult (if present) coded as: level 1, and work down to the local priest.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Hierarchical Complexity'}
    my_meta_data_dic_inner_vars = {'religious_level_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of religious level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'religious_level_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of religious level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Military_levelCreate(PermissionRequiredMixin, CreateView):
    model = Military_level
    form_class = Military_levelForm
    template_name = "sc/military_level/military_level_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('military_level-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Military Level"
        context["my_exp"] = "Talking about Hierarchical Complexity, Military levels records the Military levels of a polity. Same principle as with Administrative levels. Start with the commander-in-chief coded as: level 1, and work down to the private. Even in primitive societies such as simple chiefdoms it is often possible to distinguish at least two levels – a commander and soldiers. A complex chiefdom would be coded three levels. The presence of warrior burials might be the basis for inferring the existence of a military organization. (The lowest military level is always the individual soldier)."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'military_level_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of military level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'military_level_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of military level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Military_levelUpdate(PermissionRequiredMixin, UpdateView):
    model = Military_level
    form_class = Military_levelForm
    template_name = "sc/military_level/military_level_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Military Level"

        return context

class Military_levelDelete(PermissionRequiredMixin, DeleteView):
    model = Military_level
    success_url = reverse_lazy('military_levels')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Military_levelListView(generic.ListView):
    model = Military_level
    template_name = "sc/military_level/military_level_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('military_levels')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Military Level"
        context["var_main_desc"] = "Talking about hierarchical complexity, military levels records the military levels of a polity. same principle as with administrative levels. start with the commander-in-chief coded as: level 1, and work down to the private. even in primitive societies such as simple chiefdoms it is often possible to distinguish at least two levels – a commander and soldiers. a complex chiefdom would be coded three levels. the presence of warrior burials might be the basis for inferring the existence of a military organization. (the lowest military level is always the individual soldier)."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Hierarchical Complexity"
        context["inner_vars"] = {'military_level_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of military level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'military_level_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of military level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Military_levelListViewAll(generic.ListView):
    model = Military_level
    template_name = "sc/military_level/military_level_list_all.html"

    def get_absolute_url(self):
        return reverse('military_levels_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Military_level.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Military Level"
        context["var_main_desc"] = "Talking about hierarchical complexity, military levels records the military levels of a polity. same principle as with administrative levels. start with the commander-in-chief coded as: level 1, and work down to the private. even in primitive societies such as simple chiefdoms it is often possible to distinguish at least two levels – a commander and soldiers. a complex chiefdom would be coded three levels. the presence of warrior burials might be the basis for inferring the existence of a military organization. (the lowest military level is always the individual soldier)."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Hierarchical Complexity"
        context["inner_vars"] = {'military_level_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of military level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'military_level_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of military level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Military_levelDetailView(generic.DetailView):
    model = Military_level
    template_name = "sc/military_level/military_level_detail.html"


@permission_required('admin.can_add_log_entry')
def military_level_download(request):
    items = Military_level.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="military_levels.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'military_level_from', 'military_level_to', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.military_level_from, obj.military_level_to, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def military_level_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="military_levels.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Hierarchical Complexity, Military levels records the Military levels of a polity. Same principle as with Administrative levels. Start with the commander-in-chief coded as: level 1, and work down to the private. Even in primitive societies such as simple chiefdoms it is often possible to distinguish at least two levels – a commander and soldiers. A complex chiefdom would be coded three levels. The presence of warrior burials might be the basis for inferring the existence of a military organization. (The lowest military level is always the individual soldier).', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Hierarchical Complexity'}
    my_meta_data_dic_inner_vars = {'military_level_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of military level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'military_level_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of military level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Professional_military_officerCreate(PermissionRequiredMixin, CreateView):
    model = Professional_military_officer
    form_class = Professional_military_officerForm
    template_name = "sc/professional_military_officer/professional_military_officer_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('professional_military_officer-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Professional Military Officer"
        context["my_exp"] = "Talking about Professions, Professional military officers refer to Full-time Professional military officers."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'professional_military_officer': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional military officer for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Professional_military_officerUpdate(PermissionRequiredMixin, UpdateView):
    model = Professional_military_officer
    form_class = Professional_military_officerForm
    template_name = "sc/professional_military_officer/professional_military_officer_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Professional Military Officer"

        return context

class Professional_military_officerDelete(PermissionRequiredMixin, DeleteView):
    model = Professional_military_officer
    success_url = reverse_lazy('professional_military_officers')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Professional_military_officerListView(generic.ListView):
    model = Professional_military_officer
    template_name = "sc/professional_military_officer/professional_military_officer_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('professional_military_officers')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Professional Military Officer"
        context["var_main_desc"] = "Talking about professions, professional military officers refer to full-time professional military officers."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Professions"
        context["inner_vars"] = {'professional_military_officer': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional military officer for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Professional_military_officerListViewAll(generic.ListView):
    model = Professional_military_officer
    template_name = "sc/professional_military_officer/professional_military_officer_list_all.html"

    def get_absolute_url(self):
        return reverse('professional_military_officers_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Professional_military_officer.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Professional Military Officer"
        context["var_main_desc"] = "Talking about professions, professional military officers refer to full-time professional military officers."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Professions"
        context["inner_vars"] = {'professional_military_officer': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional military officer for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Professional_military_officerDetailView(generic.DetailView):
    model = Professional_military_officer
    template_name = "sc/professional_military_officer/professional_military_officer_detail.html"


@permission_required('admin.can_add_log_entry')
def professional_military_officer_download(request):
    items = Professional_military_officer.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="professional_military_officers.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'professional_military_officer', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.professional_military_officer, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def professional_military_officer_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="professional_military_officers.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Professions, Professional military officers refer to Full-time Professional military officers.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Professions'}
    my_meta_data_dic_inner_vars = {'professional_military_officer': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional military officer for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Professional_soldierCreate(PermissionRequiredMixin, CreateView):
    model = Professional_soldier
    form_class = Professional_soldierForm
    template_name = "sc/professional_soldier/professional_soldier_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('professional_soldier-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Professional Soldier"
        context["my_exp"] = "Talking about Professions, Professional soldiers refer to Full-time Professional soldiers."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'professional_soldier': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional soldier for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Professional_soldierUpdate(PermissionRequiredMixin, UpdateView):
    model = Professional_soldier
    form_class = Professional_soldierForm
    template_name = "sc/professional_soldier/professional_soldier_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Professional Soldier"

        return context

class Professional_soldierDelete(PermissionRequiredMixin, DeleteView):
    model = Professional_soldier
    success_url = reverse_lazy('professional_soldiers')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Professional_soldierListView(generic.ListView):
    model = Professional_soldier
    template_name = "sc/professional_soldier/professional_soldier_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('professional_soldiers')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Professional Soldier"
        context["var_main_desc"] = "Talking about professions, professional soldiers refer to full-time professional soldiers."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Professions"
        context["inner_vars"] = {'professional_soldier': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional soldier for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Professional_soldierListViewAll(generic.ListView):
    model = Professional_soldier
    template_name = "sc/professional_soldier/professional_soldier_list_all.html"

    def get_absolute_url(self):
        return reverse('professional_soldiers_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Professional_soldier.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Professional Soldier"
        context["var_main_desc"] = "Talking about professions, professional soldiers refer to full-time professional soldiers."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Professions"
        context["inner_vars"] = {'professional_soldier': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional soldier for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Professional_soldierDetailView(generic.DetailView):
    model = Professional_soldier
    template_name = "sc/professional_soldier/professional_soldier_detail.html"


@permission_required('admin.can_add_log_entry')
def professional_soldier_download(request):
    items = Professional_soldier.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="professional_soldiers.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'professional_soldier', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.professional_soldier, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def professional_soldier_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="professional_soldiers.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Professions, Professional soldiers refer to Full-time Professional soldiers.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Professions'}
    my_meta_data_dic_inner_vars = {'professional_soldier': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional soldier for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Professional_priesthoodCreate(PermissionRequiredMixin, CreateView):
    model = Professional_priesthood
    form_class = Professional_priesthoodForm
    template_name = "sc/professional_priesthood/professional_priesthood_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('professional_priesthood-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Professional Priesthood"
        context["my_exp"] = "Talking about Professions, Professional priesthood refers to Full-time Professional priesthood."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'professional_priesthood': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional priesthood for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Professional_priesthoodUpdate(PermissionRequiredMixin, UpdateView):
    model = Professional_priesthood
    form_class = Professional_priesthoodForm
    template_name = "sc/professional_priesthood/professional_priesthood_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Professional Priesthood"

        return context

class Professional_priesthoodDelete(PermissionRequiredMixin, DeleteView):
    model = Professional_priesthood
    success_url = reverse_lazy('professional_priesthoods')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Professional_priesthoodListView(generic.ListView):
    model = Professional_priesthood
    template_name = "sc/professional_priesthood/professional_priesthood_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('professional_priesthoods')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Professional Priesthood"
        context["var_main_desc"] = "Talking about professions, professional priesthood refers to full-time professional priesthood."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Professions"
        context["inner_vars"] = {'professional_priesthood': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional priesthood for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Professional_priesthoodListViewAll(generic.ListView):
    model = Professional_priesthood
    template_name = "sc/professional_priesthood/professional_priesthood_list_all.html"

    def get_absolute_url(self):
        return reverse('professional_priesthoods_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Professional_priesthood.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Professional Priesthood"
        context["var_main_desc"] = "Talking about professions, professional priesthood refers to full-time professional priesthood."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Professions"
        context["inner_vars"] = {'professional_priesthood': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional priesthood for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Professional_priesthoodDetailView(generic.DetailView):
    model = Professional_priesthood
    template_name = "sc/professional_priesthood/professional_priesthood_detail.html"


@permission_required('admin.can_add_log_entry')
def professional_priesthood_download(request):
    items = Professional_priesthood.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="professional_priesthoods.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'professional_priesthood', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.professional_priesthood, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def professional_priesthood_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="professional_priesthoods.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Professions, Professional priesthood refers to Full-time Professional priesthood.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Professions'}
    my_meta_data_dic_inner_vars = {'professional_priesthood': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional priesthood for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Full_time_bureaucratCreate(PermissionRequiredMixin, CreateView):
    model = Full_time_bureaucrat
    form_class = Full_time_bureaucratForm
    template_name = "sc/full_time_bureaucrat/full_time_bureaucrat_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('full_time_bureaucrat-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Full Time Bureaucrat"
        context["my_exp"] = "Talking about Bureaucracy characteristics, Full-time bureaucrats refer to Full-time administrative specialists. Code this absent if administrative duties are performed by generalists such as chiefs and subchiefs. Also code it absent if state officials perform multiple functions, e.g. combining administrative tasks with military duties. Note that this variable shouldn't be coded 'present' only on the basis of the presence of specialized government buildings; there must be some additional evidence of functional specialization in government."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'full_time_bureaucrat': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of full time bureaucrat for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Full_time_bureaucratUpdate(PermissionRequiredMixin, UpdateView):
    model = Full_time_bureaucrat
    form_class = Full_time_bureaucratForm
    template_name = "sc/full_time_bureaucrat/full_time_bureaucrat_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Full Time Bureaucrat"

        return context

class Full_time_bureaucratDelete(PermissionRequiredMixin, DeleteView):
    model = Full_time_bureaucrat
    success_url = reverse_lazy('full_time_bureaucrats')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Full_time_bureaucratListView(generic.ListView):
    model = Full_time_bureaucrat
    template_name = "sc/full_time_bureaucrat/full_time_bureaucrat_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('full_time_bureaucrats')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Full Time Bureaucrat"
        context["var_main_desc"] = "Talking about bureaucracy characteristics, full-time bureaucrats refer to full-time administrative specialists. code this absent if administrative duties are performed by generalists such as chiefs and subchiefs. also code it absent if state officials perform multiple functions, e.g. combining administrative tasks with military duties. note that this variable shouldn't be coded 'present' only on the basis of the presence of specialized government buildings; there must be some additional evidence of functional specialization in government."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Bureaucracy characteristics"
        context["inner_vars"] = {'full_time_bureaucrat': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of full time bureaucrat for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Full_time_bureaucratListViewAll(generic.ListView):
    model = Full_time_bureaucrat
    template_name = "sc/full_time_bureaucrat/full_time_bureaucrat_list_all.html"

    def get_absolute_url(self):
        return reverse('full_time_bureaucrats_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Full_time_bureaucrat.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Full Time Bureaucrat"
        context["var_main_desc"] = "Talking about bureaucracy characteristics, full-time bureaucrats refer to full-time administrative specialists. code this absent if administrative duties are performed by generalists such as chiefs and subchiefs. also code it absent if state officials perform multiple functions, e.g. combining administrative tasks with military duties. note that this variable shouldn't be coded 'present' only on the basis of the presence of specialized government buildings; there must be some additional evidence of functional specialization in government."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Bureaucracy characteristics"
        context["inner_vars"] = {'full_time_bureaucrat': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of full time bureaucrat for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Full_time_bureaucratDetailView(generic.DetailView):
    model = Full_time_bureaucrat
    template_name = "sc/full_time_bureaucrat/full_time_bureaucrat_detail.html"


@permission_required('admin.can_add_log_entry')
def full_time_bureaucrat_download(request):
    items = Full_time_bureaucrat.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="full_time_bureaucrats.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'full_time_bureaucrat', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.full_time_bureaucrat, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def full_time_bureaucrat_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="full_time_bureaucrats.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': "Talking about Bureaucracy characteristics, Full-time bureaucrats refer to Full-time administrative specialists. Code this absent if administrative duties are performed by generalists such as chiefs and subchiefs. Also code it absent if state officials perform multiple functions, e.g. combining administrative tasks with military duties. Note that this variable shouldn't be coded 'present' only on the basis of the presence of specialized government buildings; there must be some additional evidence of functional specialization in government.", 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Bureaucracy characteristics'}
    my_meta_data_dic_inner_vars = {'full_time_bureaucrat': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of full time bureaucrat for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Examination_systemCreate(PermissionRequiredMixin, CreateView):
    model = Examination_system
    form_class = Examination_systemForm
    template_name = "sc/examination_system/examination_system_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('examination_system-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Examination System"
        context["my_exp"] = "Talking about Bureaucracy characteristics, The paradigmatic example of an Examination system is the Chinese imperial system."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'examination_system': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of examination system for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Examination_systemUpdate(PermissionRequiredMixin, UpdateView):
    model = Examination_system
    form_class = Examination_systemForm
    template_name = "sc/examination_system/examination_system_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Examination System"

        return context

class Examination_systemDelete(PermissionRequiredMixin, DeleteView):
    model = Examination_system
    success_url = reverse_lazy('examination_systems')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Examination_systemListView(generic.ListView):
    model = Examination_system
    template_name = "sc/examination_system/examination_system_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('examination_systems')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Examination System"
        context["var_main_desc"] = "Talking about bureaucracy characteristics, the paradigmatic example of an examination system is the chinese imperial system."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Bureaucracy characteristics"
        context["inner_vars"] = {'examination_system': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of examination system for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Examination_systemListViewAll(generic.ListView):
    model = Examination_system
    template_name = "sc/examination_system/examination_system_list_all.html"

    def get_absolute_url(self):
        return reverse('examination_systems_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Examination_system.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Examination System"
        context["var_main_desc"] = "Talking about bureaucracy characteristics, the paradigmatic example of an examination system is the chinese imperial system."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Bureaucracy characteristics"
        context["inner_vars"] = {'examination_system': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of examination system for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Examination_systemDetailView(generic.DetailView):
    model = Examination_system
    template_name = "sc/examination_system/examination_system_detail.html"


@permission_required('admin.can_add_log_entry')
def examination_system_download(request):
    items = Examination_system.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="examination_systems.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'examination_system', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.examination_system, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def examination_system_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="examination_systems.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Bureaucracy characteristics, The paradigmatic example of an Examination system is the Chinese imperial system.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Bureaucracy characteristics'}
    my_meta_data_dic_inner_vars = {'examination_system': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of examination system for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Merit_promotionCreate(PermissionRequiredMixin, CreateView):
    model = Merit_promotion
    form_class = Merit_promotionForm
    template_name = "sc/merit_promotion/merit_promotion_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('merit_promotion-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Merit Promotion"
        context["my_exp"] = "Talking about Bureaucracy characteristics, Merit promotion is coded present if there are regular, institutionalized procedures for promotion based on performance. When exceptional individuals are promoted to the top ranks, in the absence of institutionalized procedures, we code it under institution and equity variables"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'merit_promotion': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of merit promotion for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Merit_promotionUpdate(PermissionRequiredMixin, UpdateView):
    model = Merit_promotion
    form_class = Merit_promotionForm
    template_name = "sc/merit_promotion/merit_promotion_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Merit Promotion"

        return context

class Merit_promotionDelete(PermissionRequiredMixin, DeleteView):
    model = Merit_promotion
    success_url = reverse_lazy('merit_promotions')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Merit_promotionListView(generic.ListView):
    model = Merit_promotion
    template_name = "sc/merit_promotion/merit_promotion_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('merit_promotions')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Merit Promotion"
        context["var_main_desc"] = "Talking about bureaucracy characteristics, merit promotion is coded present if there are regular, institutionalized procedures for promotion based on performance. when exceptional individuals are promoted to the top ranks, in the absence of institutionalized procedures, we code it under institution and equity variables"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Bureaucracy characteristics"
        context["inner_vars"] = {'merit_promotion': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of merit promotion for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Merit_promotionListViewAll(generic.ListView):
    model = Merit_promotion
    template_name = "sc/merit_promotion/merit_promotion_list_all.html"

    def get_absolute_url(self):
        return reverse('merit_promotions_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Merit_promotion.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Merit Promotion"
        context["var_main_desc"] = "Talking about bureaucracy characteristics, merit promotion is coded present if there are regular, institutionalized procedures for promotion based on performance. when exceptional individuals are promoted to the top ranks, in the absence of institutionalized procedures, we code it under institution and equity variables"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Bureaucracy characteristics"
        context["inner_vars"] = {'merit_promotion': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of merit promotion for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Merit_promotionDetailView(generic.DetailView):
    model = Merit_promotion
    template_name = "sc/merit_promotion/merit_promotion_detail.html"


@permission_required('admin.can_add_log_entry')
def merit_promotion_download(request):
    items = Merit_promotion.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="merit_promotions.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'merit_promotion', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.merit_promotion, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def merit_promotion_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="merit_promotions.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Bureaucracy characteristics, Merit promotion is coded present if there are regular, institutionalized procedures for promotion based on performance. When exceptional individuals are promoted to the top ranks, in the absence of institutionalized procedures, we code it under institution and equity variables', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Bureaucracy characteristics'}
    my_meta_data_dic_inner_vars = {'merit_promotion': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of merit promotion for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Specialized_government_buildingCreate(PermissionRequiredMixin, CreateView):
    model = Specialized_government_building
    form_class = Specialized_government_buildingForm
    template_name = "sc/specialized_government_building/specialized_government_building_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('specialized_government_building-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Specialized Government Building"
        context["my_exp"] = "Talking about Bureaucracy characteristics, These buildings are where administrative officials are located, and must be distinct from the ruler's palace. They may be used for document storage, registration offices, minting money, etc. Defense structures also are not coded here (see Military). State-owned/operated workshop should also not be coded here."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'specialized_government_building': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of specialized government building for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Specialized_government_buildingUpdate(PermissionRequiredMixin, UpdateView):
    model = Specialized_government_building
    form_class = Specialized_government_buildingForm
    template_name = "sc/specialized_government_building/specialized_government_building_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Specialized Government Building"

        return context

class Specialized_government_buildingDelete(PermissionRequiredMixin, DeleteView):
    model = Specialized_government_building
    success_url = reverse_lazy('specialized_government_buildings')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Specialized_government_buildingListView(generic.ListView):
    model = Specialized_government_building
    template_name = "sc/specialized_government_building/specialized_government_building_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('specialized_government_buildings')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Specialized Government Building"
        context["var_main_desc"] = "Talking about bureaucracy characteristics, these buildings are where administrative officials are located, and must be distinct from the ruler's palace. they may be used for document storage, registration offices, minting money, etc. defense structures also are not coded here (see military). state-owned/operated workshop should also not be coded here."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Bureaucracy characteristics"
        context["inner_vars"] = {'specialized_government_building': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of specialized government building for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Specialized_government_buildingListViewAll(generic.ListView):
    model = Specialized_government_building
    template_name = "sc/specialized_government_building/specialized_government_building_list_all.html"

    def get_absolute_url(self):
        return reverse('specialized_government_buildings_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Specialized_government_building.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Specialized Government Building"
        context["var_main_desc"] = "Talking about bureaucracy characteristics, these buildings are where administrative officials are located, and must be distinct from the ruler's palace. they may be used for document storage, registration offices, minting money, etc. defense structures also are not coded here (see military). state-owned/operated workshop should also not be coded here."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Bureaucracy characteristics"
        context["inner_vars"] = {'specialized_government_building': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of specialized government building for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Specialized_government_buildingDetailView(generic.DetailView):
    model = Specialized_government_building
    template_name = "sc/specialized_government_building/specialized_government_building_detail.html"


@permission_required('admin.can_add_log_entry')
def specialized_government_building_download(request):
    items = Specialized_government_building.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="specialized_government_buildings.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'specialized_government_building', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.specialized_government_building, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def specialized_government_building_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="specialized_government_buildings.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': "Talking about Bureaucracy characteristics, These buildings are where administrative officials are located, and must be distinct from the ruler's palace. They may be used for document storage, registration offices, minting money, etc. Defense structures also are not coded here (see Military). State-owned/operated workshop should also not be coded here.", 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Bureaucracy characteristics'}
    my_meta_data_dic_inner_vars = {'specialized_government_building': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of specialized government building for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Formal_legal_codeCreate(PermissionRequiredMixin, CreateView):
    model = Formal_legal_code
    form_class = Formal_legal_codeForm
    template_name = "sc/formal_legal_code/formal_legal_code_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('formal_legal_code-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Formal Legal Code"
        context["my_exp"] = "Talking about Law, Formal legal code refers to legal code usually, but not always written down. If not written down, code it 'present' when a uniform legal system is established by oral transmission (e.g., officials are taught the rules, or the laws are announced in a public space). Provide a short description"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'formal_legal_code': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of formal legal code for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Formal_legal_codeUpdate(PermissionRequiredMixin, UpdateView):
    model = Formal_legal_code
    form_class = Formal_legal_codeForm
    template_name = "sc/formal_legal_code/formal_legal_code_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Formal Legal Code"

        return context

class Formal_legal_codeDelete(PermissionRequiredMixin, DeleteView):
    model = Formal_legal_code
    success_url = reverse_lazy('formal_legal_codes')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Formal_legal_codeListView(generic.ListView):
    model = Formal_legal_code
    template_name = "sc/formal_legal_code/formal_legal_code_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('formal_legal_codes')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Formal Legal Code"
        context["var_main_desc"] = "Talking about law, formal legal code refers to legal code usually, but not always written down. if not written down, code it 'present' when a uniform legal system is established by oral transmission (e.g., officials are taught the rules, or the laws are announced in a public space). provide a short description"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Law"
        context["inner_vars"] = {'formal_legal_code': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of formal legal code for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Formal_legal_codeListViewAll(generic.ListView):
    model = Formal_legal_code
    template_name = "sc/formal_legal_code/formal_legal_code_list_all.html"

    def get_absolute_url(self):
        return reverse('formal_legal_codes_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Formal_legal_code.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Formal Legal Code"
        context["var_main_desc"] = "Talking about law, formal legal code refers to legal code usually, but not always written down. if not written down, code it 'present' when a uniform legal system is established by oral transmission (e.g., officials are taught the rules, or the laws are announced in a public space). provide a short description"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Law"
        context["inner_vars"] = {'formal_legal_code': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of formal legal code for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Formal_legal_codeDetailView(generic.DetailView):
    model = Formal_legal_code
    template_name = "sc/formal_legal_code/formal_legal_code_detail.html"


@permission_required('admin.can_add_log_entry')
def formal_legal_code_download(request):
    items = Formal_legal_code.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="formal_legal_codes.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'formal_legal_code', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.formal_legal_code, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def formal_legal_code_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="formal_legal_codes.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': "Talking about Law, Formal legal code refers to legal code usually, but not always written down. If not written down, code it 'present' when a uniform legal system is established by oral transmission (e.g., officials are taught the rules, or the laws are announced in a public space). Provide a short description", 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Law'}
    my_meta_data_dic_inner_vars = {'formal_legal_code': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of formal legal code for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class JudgeCreate(PermissionRequiredMixin, CreateView):
    model = Judge
    form_class = JudgeForm
    template_name = "sc/judge/judge_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('judge-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Judge"
        context["my_exp"] = "Talking about Law, judges refers only to full-time professional judges"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'judge': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of judge for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class JudgeUpdate(PermissionRequiredMixin, UpdateView):
    model = Judge
    form_class = JudgeForm
    template_name = "sc/judge/judge_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Judge"

        return context

class JudgeDelete(PermissionRequiredMixin, DeleteView):
    model = Judge
    success_url = reverse_lazy('judges')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class JudgeListView(generic.ListView):
    model = Judge
    template_name = "sc/judge/judge_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('judges')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Judge"
        context["var_main_desc"] = "Talking about law, judges refers only to full-time professional judges"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Law"
        context["inner_vars"] = {'judge': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of judge for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class JudgeListViewAll(generic.ListView):
    model = Judge
    template_name = "sc/judge/judge_list_all.html"

    def get_absolute_url(self):
        return reverse('judges_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Judge.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Judge"
        context["var_main_desc"] = "Talking about law, judges refers only to full-time professional judges"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Law"
        context["inner_vars"] = {'judge': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of judge for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class JudgeDetailView(generic.DetailView):
    model = Judge
    template_name = "sc/judge/judge_detail.html"


@permission_required('admin.can_add_log_entry')
def judge_download(request):
    items = Judge.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="judges.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'judge', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.judge, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def judge_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="judges.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Law, judges refers only to full-time professional judges', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Law'}
    my_meta_data_dic_inner_vars = {'judge': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of judge for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class CourtCreate(PermissionRequiredMixin, CreateView):
    model = Court
    form_class = CourtForm
    template_name = "sc/court/court_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('court-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Court"
        context["my_exp"] = "Talking about Law, courts are buildings specialized for legal proceedings only."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'court': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of court for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class CourtUpdate(PermissionRequiredMixin, UpdateView):
    model = Court
    form_class = CourtForm
    template_name = "sc/court/court_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Court"

        return context

class CourtDelete(PermissionRequiredMixin, DeleteView):
    model = Court
    success_url = reverse_lazy('courts')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class CourtListView(generic.ListView):
    model = Court
    template_name = "sc/court/court_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('courts')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Court"
        context["var_main_desc"] = "Talking about law, courts are buildings specialized for legal proceedings only."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Law"
        context["inner_vars"] = {'court': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of court for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class CourtListViewAll(generic.ListView):
    model = Court
    template_name = "sc/court/court_list_all.html"

    def get_absolute_url(self):
        return reverse('courts_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Court.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Court"
        context["var_main_desc"] = "Talking about law, courts are buildings specialized for legal proceedings only."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Law"
        context["inner_vars"] = {'court': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of court for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class CourtDetailView(generic.DetailView):
    model = Court
    template_name = "sc/court/court_detail.html"


@permission_required('admin.can_add_log_entry')
def court_download(request):
    items = Court.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="courts.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'court', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.court, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def court_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="courts.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Law, courts are buildings specialized for legal proceedings only.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Law'}
    my_meta_data_dic_inner_vars = {'court': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of court for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Professional_lawyerCreate(PermissionRequiredMixin, CreateView):
    model = Professional_lawyer
    form_class = Professional_lawyerForm
    template_name = "sc/professional_lawyer/professional_lawyer_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('professional_lawyer-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Professional Lawyer"
        context["my_exp"] = "Talking about Law, NO_DESCRIPTIONS_IN_CODEBOOK."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'professional_lawyer': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional lawyer for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Professional_lawyerUpdate(PermissionRequiredMixin, UpdateView):
    model = Professional_lawyer
    form_class = Professional_lawyerForm
    template_name = "sc/professional_lawyer/professional_lawyer_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Professional Lawyer"

        return context

class Professional_lawyerDelete(PermissionRequiredMixin, DeleteView):
    model = Professional_lawyer
    success_url = reverse_lazy('professional_lawyers')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Professional_lawyerListView(generic.ListView):
    model = Professional_lawyer
    template_name = "sc/professional_lawyer/professional_lawyer_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('professional_lawyers')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Professional Lawyer"
        context["var_main_desc"] = "Talking about law, no Descriptions IN Codebook."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Law"
        context["inner_vars"] = {'professional_lawyer': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional lawyer for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Professional_lawyerListViewAll(generic.ListView):
    model = Professional_lawyer
    template_name = "sc/professional_lawyer/professional_lawyer_list_all.html"

    def get_absolute_url(self):
        return reverse('professional_lawyers_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Professional_lawyer.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Professional Lawyer"
        context["var_main_desc"] = "Talking about law, no Descriptions IN Codebook."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Law"
        context["inner_vars"] = {'professional_lawyer': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional lawyer for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Professional_lawyerDetailView(generic.DetailView):
    model = Professional_lawyer
    template_name = "sc/professional_lawyer/professional_lawyer_detail.html"


@permission_required('admin.can_add_log_entry')
def professional_lawyer_download(request):
    items = Professional_lawyer.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="professional_lawyers.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'professional_lawyer', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.professional_lawyer, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def professional_lawyer_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="professional_lawyers.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Law, NO_DESCRIPTIONS_IN_CODEBOOK.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Law'}
    my_meta_data_dic_inner_vars = {'professional_lawyer': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional lawyer for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Irrigation_systemCreate(PermissionRequiredMixin, CreateView):
    model = Irrigation_system
    form_class = Irrigation_systemForm
    template_name = "sc/irrigation_system/irrigation_system_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('irrigation_system-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Irrigation System"
        context["my_exp"] = "Talking about Specialized Buildings, irrigation systems are polity owned (which includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'irrigation_system': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of irrigation system for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Irrigation_systemUpdate(PermissionRequiredMixin, UpdateView):
    model = Irrigation_system
    form_class = Irrigation_systemForm
    template_name = "sc/irrigation_system/irrigation_system_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Irrigation System"

        return context

class Irrigation_systemDelete(PermissionRequiredMixin, DeleteView):
    model = Irrigation_system
    success_url = reverse_lazy('irrigation_systems')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Irrigation_systemListView(generic.ListView):
    model = Irrigation_system
    template_name = "sc/irrigation_system/irrigation_system_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('irrigation_systems')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Irrigation System"
        context["var_main_desc"] = "Talking about specialized buildings, irrigation systems are polity owned (which includes owned by the community, or the state), no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Specialized Buildings"
        context["inner_vars"] = {'irrigation_system': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of irrigation system for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Irrigation_systemListViewAll(generic.ListView):
    model = Irrigation_system
    template_name = "sc/irrigation_system/irrigation_system_list_all.html"

    def get_absolute_url(self):
        return reverse('irrigation_systems_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Irrigation_system.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Irrigation System"
        context["var_main_desc"] = "Talking about specialized buildings, irrigation systems are polity owned (which includes owned by the community, or the state), no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Specialized Buildings"
        context["inner_vars"] = {'irrigation_system': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of irrigation system for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Irrigation_systemDetailView(generic.DetailView):
    model = Irrigation_system
    template_name = "sc/irrigation_system/irrigation_system_detail.html"


@permission_required('admin.can_add_log_entry')
def irrigation_system_download(request):
    items = Irrigation_system.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="irrigation_systems.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'irrigation_system', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.irrigation_system, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def irrigation_system_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="irrigation_systems.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Specialized Buildings, irrigation systems are polity owned (which includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Specialized Buildings'}
    my_meta_data_dic_inner_vars = {'irrigation_system': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of irrigation system for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Drinking_water_supply_systemCreate(PermissionRequiredMixin, CreateView):
    model = Drinking_water_supply_system
    form_class = Drinking_water_supply_systemForm
    template_name = "sc/drinking_water_supply_system/drinking_water_supply_system_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('drinking_water_supply_system-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Drinking Water Supply System"
        context["my_exp"] = "Talking about Specialized Buildings, drinking water supply systems are polity owned (which includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'drinking_water_supply_system': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of drinking water supply system for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Drinking_water_supply_systemUpdate(PermissionRequiredMixin, UpdateView):
    model = Drinking_water_supply_system
    form_class = Drinking_water_supply_systemForm
    template_name = "sc/drinking_water_supply_system/drinking_water_supply_system_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Drinking Water Supply System"

        return context

class Drinking_water_supply_systemDelete(PermissionRequiredMixin, DeleteView):
    model = Drinking_water_supply_system
    success_url = reverse_lazy('drinking_water_supply_systems')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Drinking_water_supply_systemListView(generic.ListView):
    model = Drinking_water_supply_system
    template_name = "sc/drinking_water_supply_system/drinking_water_supply_system_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('drinking_water_supply_systems')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Drinking Water Supply System"
        context["var_main_desc"] = "Talking about specialized buildings, drinking water supply systems are polity owned (which includes owned by the community, or the state), no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Specialized Buildings"
        context["inner_vars"] = {'drinking_water_supply_system': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of drinking water supply system for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Drinking_water_supply_systemListViewAll(generic.ListView):
    model = Drinking_water_supply_system
    template_name = "sc/drinking_water_supply_system/drinking_water_supply_system_list_all.html"

    def get_absolute_url(self):
        return reverse('drinking_water_supply_systems_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Drinking_water_supply_system.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Drinking Water Supply System"
        context["var_main_desc"] = "Talking about specialized buildings, drinking water supply systems are polity owned (which includes owned by the community, or the state), no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Specialized Buildings"
        context["inner_vars"] = {'drinking_water_supply_system': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of drinking water supply system for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Drinking_water_supply_systemDetailView(generic.DetailView):
    model = Drinking_water_supply_system
    template_name = "sc/drinking_water_supply_system/drinking_water_supply_system_detail.html"


@permission_required('admin.can_add_log_entry')
def drinking_water_supply_system_download(request):
    items = Drinking_water_supply_system.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="drinking_water_supply_systems.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'drinking_water_supply_system', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.drinking_water_supply_system, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def drinking_water_supply_system_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="drinking_water_supply_systems.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Specialized Buildings, drinking water supply systems are polity owned (which includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Specialized Buildings'}
    my_meta_data_dic_inner_vars = {'drinking_water_supply_system': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of drinking water supply system for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class MarketCreate(PermissionRequiredMixin, CreateView):
    model = Market
    form_class = MarketForm
    template_name = "sc/market/market_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('market-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Market"
        context["my_exp"] = "Talking about Specialized Buildings, markets are polity owned (which includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'market': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of market for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class MarketUpdate(PermissionRequiredMixin, UpdateView):
    model = Market
    form_class = MarketForm
    template_name = "sc/market/market_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Market"

        return context

class MarketDelete(PermissionRequiredMixin, DeleteView):
    model = Market
    success_url = reverse_lazy('markets')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class MarketListView(generic.ListView):
    model = Market
    template_name = "sc/market/market_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('markets')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Market"
        context["var_main_desc"] = "Talking about specialized buildings, markets are polity owned (which includes owned by the community, or the state), no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Specialized Buildings"
        context["inner_vars"] = {'market': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of market for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class MarketListViewAll(generic.ListView):
    model = Market
    template_name = "sc/market/market_list_all.html"

    def get_absolute_url(self):
        return reverse('markets_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Market.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Market"
        context["var_main_desc"] = "Talking about specialized buildings, markets are polity owned (which includes owned by the community, or the state), no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Specialized Buildings"
        context["inner_vars"] = {'market': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of market for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class MarketDetailView(generic.DetailView):
    model = Market
    template_name = "sc/market/market_detail.html"


@permission_required('admin.can_add_log_entry')
def market_download(request):
    items = Market.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="markets.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'market', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.market, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def market_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="markets.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Specialized Buildings, markets are polity owned (which includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Specialized Buildings'}
    my_meta_data_dic_inner_vars = {'market': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of market for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Food_storage_siteCreate(PermissionRequiredMixin, CreateView):
    model = Food_storage_site
    form_class = Food_storage_siteForm
    template_name = "sc/food_storage_site/food_storage_site_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('food_storage_site-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Food Storage Site"
        context["my_exp"] = "Talking about Specialized Buildings, food storage sites are polity owned (which  includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'food_storage_site': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of food storage site for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Food_storage_siteUpdate(PermissionRequiredMixin, UpdateView):
    model = Food_storage_site
    form_class = Food_storage_siteForm
    template_name = "sc/food_storage_site/food_storage_site_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Food Storage Site"

        return context

class Food_storage_siteDelete(PermissionRequiredMixin, DeleteView):
    model = Food_storage_site
    success_url = reverse_lazy('food_storage_sites')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Food_storage_siteListView(generic.ListView):
    model = Food_storage_site
    template_name = "sc/food_storage_site/food_storage_site_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('food_storage_sites')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Food Storage Site"
        context["var_main_desc"] = "Talking about specialized buildings, food storage sites are polity owned (which  includes owned by the community, or the state), no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Specialized Buildings"
        context["inner_vars"] = {'food_storage_site': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of food storage site for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Food_storage_siteListViewAll(generic.ListView):
    model = Food_storage_site
    template_name = "sc/food_storage_site/food_storage_site_list_all.html"

    def get_absolute_url(self):
        return reverse('food_storage_sites_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Food_storage_site.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Food Storage Site"
        context["var_main_desc"] = "Talking about specialized buildings, food storage sites are polity owned (which  includes owned by the community, or the state), no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Specialized Buildings"
        context["inner_vars"] = {'food_storage_site': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of food storage site for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Food_storage_siteDetailView(generic.DetailView):
    model = Food_storage_site
    template_name = "sc/food_storage_site/food_storage_site_detail.html"


@permission_required('admin.can_add_log_entry')
def food_storage_site_download(request):
    items = Food_storage_site.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="food_storage_sites.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'food_storage_site', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.food_storage_site, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def food_storage_site_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="food_storage_sites.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Specialized Buildings, food storage sites are polity owned (which  includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Specialized Buildings'}
    my_meta_data_dic_inner_vars = {'food_storage_site': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of food storage site for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class RoadCreate(PermissionRequiredMixin, CreateView):
    model = Road
    form_class = RoadForm
    template_name = "sc/road/road_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('road-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Road"
        context["my_exp"] = "Talking about Transport infrastructure, roads refers to deliberately constructed roads that connect settlements or other sites. It excludes streets/accessways within settlements and paths between settlements that develop through repeated use."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'road': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of road for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class RoadUpdate(PermissionRequiredMixin, UpdateView):
    model = Road
    form_class = RoadForm
    template_name = "sc/road/road_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Road"

        return context

class RoadDelete(PermissionRequiredMixin, DeleteView):
    model = Road
    success_url = reverse_lazy('roads')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class RoadListView(generic.ListView):
    model = Road
    template_name = "sc/road/road_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('roads')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Road"
        context["var_main_desc"] = "Talking about transport infrastructure, roads refers to deliberately constructed roads that connect settlements or other sites. it excludes streets/accessways within settlements and paths between settlements that develop through repeated use."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Transport infrastructure"
        context["inner_vars"] = {'road': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of road for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class RoadListViewAll(generic.ListView):
    model = Road
    template_name = "sc/road/road_list_all.html"

    def get_absolute_url(self):
        return reverse('roads_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Road.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Road"
        context["var_main_desc"] = "Talking about transport infrastructure, roads refers to deliberately constructed roads that connect settlements or other sites. it excludes streets/accessways within settlements and paths between settlements that develop through repeated use."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Transport infrastructure"
        context["inner_vars"] = {'road': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of road for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class RoadDetailView(generic.DetailView):
    model = Road
    template_name = "sc/road/road_detail.html"


@permission_required('admin.can_add_log_entry')
def road_download(request):
    items = Road.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="roads.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'road', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.road, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def road_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="roads.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Transport infrastructure, roads refers to deliberately constructed roads that connect settlements or other sites. It excludes streets/accessways within settlements and paths between settlements that develop through repeated use.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Transport infrastructure'}
    my_meta_data_dic_inner_vars = {'road': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of road for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class BridgeCreate(PermissionRequiredMixin, CreateView):
    model = Bridge
    form_class = BridgeForm
    template_name = "sc/bridge/bridge_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('bridge-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Bridge"
        context["my_exp"] = "Talking about Transport infrastructure, bridges refers to bridges built and/or maintained by the polity (that is, code 'present' even if the polity did not build a bridge, but devotes resources to maintaining it)."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'bridge': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of bridge for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class BridgeUpdate(PermissionRequiredMixin, UpdateView):
    model = Bridge
    form_class = BridgeForm
    template_name = "sc/bridge/bridge_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Bridge"

        return context

class BridgeDelete(PermissionRequiredMixin, DeleteView):
    model = Bridge
    success_url = reverse_lazy('bridges')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class BridgeListView(generic.ListView):
    model = Bridge
    template_name = "sc/bridge/bridge_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('bridges')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Bridge"
        context["var_main_desc"] = "Talking about transport infrastructure, bridges refers to bridges built and/or maintained by the polity (that is, code 'present' even if the polity did not build a bridge, but devotes resources to maintaining it)."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Transport infrastructure"
        context["inner_vars"] = {'bridge': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of bridge for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class BridgeListViewAll(generic.ListView):
    model = Bridge
    template_name = "sc/bridge/bridge_list_all.html"

    def get_absolute_url(self):
        return reverse('bridges_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Bridge.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Bridge"
        context["var_main_desc"] = "Talking about transport infrastructure, bridges refers to bridges built and/or maintained by the polity (that is, code 'present' even if the polity did not build a bridge, but devotes resources to maintaining it)."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Transport infrastructure"
        context["inner_vars"] = {'bridge': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of bridge for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class BridgeDetailView(generic.DetailView):
    model = Bridge
    template_name = "sc/bridge/bridge_detail.html"


@permission_required('admin.can_add_log_entry')
def bridge_download(request):
    items = Bridge.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="bridges.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'bridge', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.bridge, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def bridge_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="bridges.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': "Talking about Transport infrastructure, bridges refers to bridges built and/or maintained by the polity (that is, code 'present' even if the polity did not build a bridge, but devotes resources to maintaining it).", 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Transport infrastructure'}
    my_meta_data_dic_inner_vars = {'bridge': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of bridge for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class CanalCreate(PermissionRequiredMixin, CreateView):
    model = Canal
    form_class = CanalForm
    template_name = "sc/canal/canal_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('canal-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Canal"
        context["my_exp"] = "Talking about Transport infrastructure, canals refers to canals built and/or maintained by the polity (that is, code 'present' even if the polity did not build a canal, but devotes resources to maintaining it)."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'canal': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of canal for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class CanalUpdate(PermissionRequiredMixin, UpdateView):
    model = Canal
    form_class = CanalForm
    template_name = "sc/canal/canal_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Canal"

        return context

class CanalDelete(PermissionRequiredMixin, DeleteView):
    model = Canal
    success_url = reverse_lazy('canals')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class CanalListView(generic.ListView):
    model = Canal
    template_name = "sc/canal/canal_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('canals')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Canal"
        context["var_main_desc"] = "Talking about transport infrastructure, canals refers to canals built and/or maintained by the polity (that is, code 'present' even if the polity did not build a canal, but devotes resources to maintaining it)."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Transport infrastructure"
        context["inner_vars"] = {'canal': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of canal for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class CanalListViewAll(generic.ListView):
    model = Canal
    template_name = "sc/canal/canal_list_all.html"

    def get_absolute_url(self):
        return reverse('canals_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Canal.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Canal"
        context["var_main_desc"] = "Talking about transport infrastructure, canals refers to canals built and/or maintained by the polity (that is, code 'present' even if the polity did not build a canal, but devotes resources to maintaining it)."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Transport infrastructure"
        context["inner_vars"] = {'canal': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of canal for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class CanalDetailView(generic.DetailView):
    model = Canal
    template_name = "sc/canal/canal_detail.html"


@permission_required('admin.can_add_log_entry')
def canal_download(request):
    items = Canal.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="canals.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'canal', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.canal, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def canal_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="canals.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': "Talking about Transport infrastructure, canals refers to canals built and/or maintained by the polity (that is, code 'present' even if the polity did not build a canal, but devotes resources to maintaining it).", 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Transport infrastructure'}
    my_meta_data_dic_inner_vars = {'canal': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of canal for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class PortCreate(PermissionRequiredMixin, CreateView):
    model = Port
    form_class = PortForm
    template_name = "sc/port/port_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('port-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Port"
        context["my_exp"] = "Talking about Transport infrastructure, Ports include river ports. Direct historical or archaeological evidence of Ports is absent when no port has been excavated or all evidence of such has been obliterated. Indirect historical or archaeological data is absent when there is no evidence that suggests that the polity engaged in maritime or riverine trade, conflict, or transportation, such as evidence of merchant shipping, administrative records of customs duties, or evidence that at the same period of time a trading relation in the region had a port (for example, due to natural processes, there is little evidence of ancient ports in delta Egypt at a time we know there was a timber trade with the Levant). When evidence for the variable itself is available the code is 'present.' When other forms of evidence suggests the existence of the variable (or not) the code may be 'inferred present' (or 'inferred absent'). When indirect evidence is not available the code will be either absent, temporal uncertainty, suspected unknown, or unknown."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'port': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of port for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class PortUpdate(PermissionRequiredMixin, UpdateView):
    model = Port
    form_class = PortForm
    template_name = "sc/port/port_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Port"

        return context

class PortDelete(PermissionRequiredMixin, DeleteView):
    model = Port
    success_url = reverse_lazy('ports')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class PortListView(generic.ListView):
    model = Port
    template_name = "sc/port/port_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('ports')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Port"
        context["var_main_desc"] = "Talking about transport infrastructure, ports include river ports. direct historical or archaeological evidence of ports is absent when no port has been excavated or all evidence of such has been obliterated. indirect historical or archaeological data is absent when there is no evidence that suggests that the polity engaged in maritime or riverine trade, conflict, or transportation, such as evidence of merchant shipping, administrative records of customs duties, or evidence that at the same period of time a trading relation in the region had a port (for example, due to natural processes, there is little evidence of ancient ports in delta egypt at a time we know there was a timber trade with the levant). when evidence for the variable itself is available the code is 'present.' when other forms of evidence suggests the existence of the variable (or not) the code may be 'inferred present' (or 'inferred absent'). when indirect evidence is not available the code will be either absent, temporal uncertainty, suspected unknown, or unknown."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Transport infrastructure"
        context["inner_vars"] = {'port': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of port for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class PortListViewAll(generic.ListView):
    model = Port
    template_name = "sc/port/port_list_all.html"

    def get_absolute_url(self):
        return reverse('ports_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Port.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Port"
        context["var_main_desc"] = "Talking about transport infrastructure, ports include river ports. direct historical or archaeological evidence of ports is absent when no port has been excavated or all evidence of such has been obliterated. indirect historical or archaeological data is absent when there is no evidence that suggests that the polity engaged in maritime or riverine trade, conflict, or transportation, such as evidence of merchant shipping, administrative records of customs duties, or evidence that at the same period of time a trading relation in the region had a port (for example, due to natural processes, there is little evidence of ancient ports in delta egypt at a time we know there was a timber trade with the levant). when evidence for the variable itself is available the code is 'present.' when other forms of evidence suggests the existence of the variable (or not) the code may be 'inferred present' (or 'inferred absent'). when indirect evidence is not available the code will be either absent, temporal uncertainty, suspected unknown, or unknown."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Transport infrastructure"
        context["inner_vars"] = {'port': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of port for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class PortDetailView(generic.DetailView):
    model = Port
    template_name = "sc/port/port_detail.html"


@permission_required('admin.can_add_log_entry')
def port_download(request):
    items = Port.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ports.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'port', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.port, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def port_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ports.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': "Talking about Transport infrastructure, Ports include river ports. Direct historical or archaeological evidence of Ports is absent when no port has been excavated or all evidence of such has been obliterated. Indirect historical or archaeological data is absent when there is no evidence that suggests that the polity engaged in maritime or riverine trade, conflict, or transportation, such as evidence of merchant shipping, administrative records of customs duties, or evidence that at the same period of time a trading relation in the region had a port (for example, due to natural processes, there is little evidence of ancient ports in delta Egypt at a time we know there was a timber trade with the Levant). When evidence for the variable itself is available the code is 'present.' When other forms of evidence suggests the existence of the variable (or not) the code may be 'inferred present' (or 'inferred absent'). When indirect evidence is not available the code will be either absent, temporal uncertainty, suspected unknown, or unknown.", 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Transport infrastructure'}
    my_meta_data_dic_inner_vars = {'port': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of port for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Mines_or_quarryCreate(PermissionRequiredMixin, CreateView):
    model = Mines_or_quarry
    form_class = Mines_or_quarryForm
    template_name = "sc/mines_or_quarry/mines_or_quarry_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('mines_or_quarry-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Mines or Quarry"
        context["my_exp"] = "Talking about Special purpose sites, NO_DESCRIPTIONS_IN_CODEBOOK"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'mines_or_quarry': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of mines or quarry for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Mines_or_quarryUpdate(PermissionRequiredMixin, UpdateView):
    model = Mines_or_quarry
    form_class = Mines_or_quarryForm
    template_name = "sc/mines_or_quarry/mines_or_quarry_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Mines or Quarry"

        return context

class Mines_or_quarryDelete(PermissionRequiredMixin, DeleteView):
    model = Mines_or_quarry
    success_url = reverse_lazy('mines_or_quarrys')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Mines_or_quarryListView(generic.ListView):
    model = Mines_or_quarry
    template_name = "sc/mines_or_quarry/mines_or_quarry_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('mines_or_quarrys')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Mines or Quarry"
        context["var_main_desc"] = "Talking about special purpose sites, no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Special purpose sites"
        context["inner_vars"] = {'mines_or_quarry': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of mines or quarry for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Mines_or_quarryListViewAll(generic.ListView):
    model = Mines_or_quarry
    template_name = "sc/mines_or_quarry/mines_or_quarry_list_all.html"

    def get_absolute_url(self):
        return reverse('mines_or_quarrys_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Mines_or_quarry.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Mines or Quarry"
        context["var_main_desc"] = "Talking about special purpose sites, no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Special purpose sites"
        context["inner_vars"] = {'mines_or_quarry': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of mines or quarry for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Mines_or_quarryDetailView(generic.DetailView):
    model = Mines_or_quarry
    template_name = "sc/mines_or_quarry/mines_or_quarry_detail.html"


@permission_required('admin.can_add_log_entry')
def mines_or_quarry_download(request):
    items = Mines_or_quarry.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mines_or_quarrys.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'mines_or_quarry', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.mines_or_quarry, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def mines_or_quarry_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mines_or_quarrys.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Special purpose sites, NO_DESCRIPTIONS_IN_CODEBOOK', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Special purpose sites'}
    my_meta_data_dic_inner_vars = {'mines_or_quarry': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of mines or quarry for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Mnemonic_deviceCreate(PermissionRequiredMixin, CreateView):
    model = Mnemonic_device
    form_class = Mnemonic_deviceForm
    template_name = "sc/mnemonic_device/mnemonic_device_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('mnemonic_device-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Mnemonic Device"
        context["my_exp"] = "Talking about Writing Systems, Mnemonic devices are: For example, tallies"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'mnemonic_device': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of mnemonic device for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Mnemonic_deviceUpdate(PermissionRequiredMixin, UpdateView):
    model = Mnemonic_device
    form_class = Mnemonic_deviceForm
    template_name = "sc/mnemonic_device/mnemonic_device_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Mnemonic Device"

        return context

class Mnemonic_deviceDelete(PermissionRequiredMixin, DeleteView):
    model = Mnemonic_device
    success_url = reverse_lazy('mnemonic_devices')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Mnemonic_deviceListView(generic.ListView):
    model = Mnemonic_device
    template_name = "sc/mnemonic_device/mnemonic_device_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('mnemonic_devices')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Mnemonic Device"
        context["var_main_desc"] = "Talking about writing systems, mnemonic devices are: for example, tallies"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Writing Systems"
        context["inner_vars"] = {'mnemonic_device': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of mnemonic device for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Mnemonic_deviceListViewAll(generic.ListView):
    model = Mnemonic_device
    template_name = "sc/mnemonic_device/mnemonic_device_list_all.html"

    def get_absolute_url(self):
        return reverse('mnemonic_devices_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Mnemonic_device.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Mnemonic Device"
        context["var_main_desc"] = "Talking about writing systems, mnemonic devices are: for example, tallies"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Writing Systems"
        context["inner_vars"] = {'mnemonic_device': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of mnemonic device for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Mnemonic_deviceDetailView(generic.DetailView):
    model = Mnemonic_device
    template_name = "sc/mnemonic_device/mnemonic_device_detail.html"


@permission_required('admin.can_add_log_entry')
def mnemonic_device_download(request):
    items = Mnemonic_device.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mnemonic_devices.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'mnemonic_device', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.mnemonic_device, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def mnemonic_device_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mnemonic_devices.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Writing Systems, Mnemonic devices are: For example, tallies', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Writing Systems'}
    my_meta_data_dic_inner_vars = {'mnemonic_device': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of mnemonic device for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Nonwritten_recordCreate(PermissionRequiredMixin, CreateView):
    model = Nonwritten_record
    form_class = Nonwritten_recordForm
    template_name = "sc/nonwritten_record/nonwritten_record_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('nonwritten_record-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Nonwritten Record"
        context["my_exp"] = "Talking about Writing Systems, Nonwritten Records are more extensive than mnemonics, but don't utilize script. Example: quipu; seals and stamps"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'nonwritten_record': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of nonwritten record for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Nonwritten_recordUpdate(PermissionRequiredMixin, UpdateView):
    model = Nonwritten_record
    form_class = Nonwritten_recordForm
    template_name = "sc/nonwritten_record/nonwritten_record_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Nonwritten Record"

        return context

class Nonwritten_recordDelete(PermissionRequiredMixin, DeleteView):
    model = Nonwritten_record
    success_url = reverse_lazy('nonwritten_records')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Nonwritten_recordListView(generic.ListView):
    model = Nonwritten_record
    template_name = "sc/nonwritten_record/nonwritten_record_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('nonwritten_records')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Nonwritten Record"
        context["var_main_desc"] = "Talking about writing systems, nonwritten records are more extensive than mnemonics, but don't utilize script. example: quipu; seals and stamps"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Writing Systems"
        context["inner_vars"] = {'nonwritten_record': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of nonwritten record for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Nonwritten_recordListViewAll(generic.ListView):
    model = Nonwritten_record
    template_name = "sc/nonwritten_record/nonwritten_record_list_all.html"

    def get_absolute_url(self):
        return reverse('nonwritten_records_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Nonwritten_record.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Nonwritten Record"
        context["var_main_desc"] = "Talking about writing systems, nonwritten records are more extensive than mnemonics, but don't utilize script. example: quipu; seals and stamps"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Writing Systems"
        context["inner_vars"] = {'nonwritten_record': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of nonwritten record for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Nonwritten_recordDetailView(generic.DetailView):
    model = Nonwritten_record
    template_name = "sc/nonwritten_record/nonwritten_record_detail.html"


@permission_required('admin.can_add_log_entry')
def nonwritten_record_download(request):
    items = Nonwritten_record.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="nonwritten_records.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'nonwritten_record', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.nonwritten_record, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def nonwritten_record_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="nonwritten_records.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': "Talking about Writing Systems, Nonwritten Records are more extensive than mnemonics, but don't utilize script. Example: quipu; seals and stamps", 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Writing Systems'}
    my_meta_data_dic_inner_vars = {'nonwritten_record': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of nonwritten record for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Written_recordCreate(PermissionRequiredMixin, CreateView):
    model = Written_record
    form_class = Written_recordForm
    template_name = "sc/written_record/written_record_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('written_record-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Written Record"
        context["my_exp"] = "Talking about Writing Systems, Written records are more than short and fragmentary inscriptions, such as found on tombs or runic stones. There must be several sentences strung together, at the very minimum. For example, royal proclamations from Mesopotamia and Egypt qualify as written records"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'written_record': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of written record for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Written_recordUpdate(PermissionRequiredMixin, UpdateView):
    model = Written_record
    form_class = Written_recordForm
    template_name = "sc/written_record/written_record_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Written Record"

        return context

class Written_recordDelete(PermissionRequiredMixin, DeleteView):
    model = Written_record
    success_url = reverse_lazy('written_records')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Written_recordListView(generic.ListView):
    model = Written_record
    template_name = "sc/written_record/written_record_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('written_records')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Written Record"
        context["var_main_desc"] = "Talking about writing systems, written records are more than short and fragmentary inscriptions, such as found on tombs or runic stones. there must be several sentences strung together, at the very minimum. for example, royal proclamations from mesopotamia and egypt qualify as written records"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Writing Systems"
        context["inner_vars"] = {'written_record': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of written record for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Written_recordListViewAll(generic.ListView):
    model = Written_record
    template_name = "sc/written_record/written_record_list_all.html"

    def get_absolute_url(self):
        return reverse('written_records_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Written_record.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Written Record"
        context["var_main_desc"] = "Talking about writing systems, written records are more than short and fragmentary inscriptions, such as found on tombs or runic stones. there must be several sentences strung together, at the very minimum. for example, royal proclamations from mesopotamia and egypt qualify as written records"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Writing Systems"
        context["inner_vars"] = {'written_record': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of written record for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Written_recordDetailView(generic.DetailView):
    model = Written_record
    template_name = "sc/written_record/written_record_detail.html"


@permission_required('admin.can_add_log_entry')
def written_record_download(request):
    items = Written_record.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="written_records.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'written_record', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.written_record, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def written_record_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="written_records.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Writing Systems, Written records are more than short and fragmentary inscriptions, such as found on tombs or runic stones. There must be several sentences strung together, at the very minimum. For example, royal proclamations from Mesopotamia and Egypt qualify as written records', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Writing Systems'}
    my_meta_data_dic_inner_vars = {'written_record': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of written record for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class ScriptCreate(PermissionRequiredMixin, CreateView):
    model = Script
    form_class = ScriptForm
    template_name = "sc/script/script_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('script-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Script"
        context["my_exp"] = "Talking about Writing Systems, script is as indicated at least by fragmentary inscriptions (note that if written records are present, then so is script)"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'script': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of script for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class ScriptUpdate(PermissionRequiredMixin, UpdateView):
    model = Script
    form_class = ScriptForm
    template_name = "sc/script/script_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Script"

        return context

class ScriptDelete(PermissionRequiredMixin, DeleteView):
    model = Script
    success_url = reverse_lazy('scripts')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class ScriptListView(generic.ListView):
    model = Script
    template_name = "sc/script/script_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('scripts')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Script"
        context["var_main_desc"] = "Talking about writing systems, script is as indicated at least by fragmentary inscriptions (note that if written records are present, then so is script)"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Writing Systems"
        context["inner_vars"] = {'script': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of script for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class ScriptListViewAll(generic.ListView):
    model = Script
    template_name = "sc/script/script_list_all.html"

    def get_absolute_url(self):
        return reverse('scripts_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Script.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Script"
        context["var_main_desc"] = "Talking about writing systems, script is as indicated at least by fragmentary inscriptions (note that if written records are present, then so is script)"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Writing Systems"
        context["inner_vars"] = {'script': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of script for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class ScriptDetailView(generic.DetailView):
    model = Script
    template_name = "sc/script/script_detail.html"


@permission_required('admin.can_add_log_entry')
def script_download(request):
    items = Script.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="scripts.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'script', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.script, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def script_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="scripts.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Writing Systems, script is as indicated at least by fragmentary inscriptions (note that if written records are present, then so is script)', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Writing Systems'}
    my_meta_data_dic_inner_vars = {'script': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of script for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Non_phonetic_writingCreate(PermissionRequiredMixin, CreateView):
    model = Non_phonetic_writing
    form_class = Non_phonetic_writingForm
    template_name = "sc/non_phonetic_writing/non_phonetic_writing_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('non_phonetic_writing-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Non Phonetic Writing"
        context["my_exp"] = "Talking about Writing Systems, this refers to the kind of script"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'non_phonetic_writing': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of non phonetic writing for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Non_phonetic_writingUpdate(PermissionRequiredMixin, UpdateView):
    model = Non_phonetic_writing
    form_class = Non_phonetic_writingForm
    template_name = "sc/non_phonetic_writing/non_phonetic_writing_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Non Phonetic Writing"

        return context

class Non_phonetic_writingDelete(PermissionRequiredMixin, DeleteView):
    model = Non_phonetic_writing
    success_url = reverse_lazy('non_phonetic_writings')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Non_phonetic_writingListView(generic.ListView):
    model = Non_phonetic_writing
    template_name = "sc/non_phonetic_writing/non_phonetic_writing_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('non_phonetic_writings')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Non Phonetic Writing"
        context["var_main_desc"] = "Talking about writing systems, this refers to the kind of script"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Writing Systems"
        context["inner_vars"] = {'non_phonetic_writing': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of non phonetic writing for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Non_phonetic_writingListViewAll(generic.ListView):
    model = Non_phonetic_writing
    template_name = "sc/non_phonetic_writing/non_phonetic_writing_list_all.html"

    def get_absolute_url(self):
        return reverse('non_phonetic_writings_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Non_phonetic_writing.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Non Phonetic Writing"
        context["var_main_desc"] = "Talking about writing systems, this refers to the kind of script"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Writing Systems"
        context["inner_vars"] = {'non_phonetic_writing': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of non phonetic writing for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Non_phonetic_writingDetailView(generic.DetailView):
    model = Non_phonetic_writing
    template_name = "sc/non_phonetic_writing/non_phonetic_writing_detail.html"


@permission_required('admin.can_add_log_entry')
def non_phonetic_writing_download(request):
    items = Non_phonetic_writing.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="non_phonetic_writings.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'non_phonetic_writing', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.non_phonetic_writing, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def non_phonetic_writing_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="non_phonetic_writings.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Writing Systems, this refers to the kind of script', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Writing Systems'}
    my_meta_data_dic_inner_vars = {'non_phonetic_writing': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of non phonetic writing for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Phonetic_alphabetic_writingCreate(PermissionRequiredMixin, CreateView):
    model = Phonetic_alphabetic_writing
    form_class = Phonetic_alphabetic_writingForm
    template_name = "sc/phonetic_alphabetic_writing/phonetic_alphabetic_writing_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('phonetic_alphabetic_writing-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Phonetic Alphabetic Writing"
        context["my_exp"] = "Talking about Writing Systems, this refers to the kind of script"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'phonetic_alphabetic_writing': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of phonetic alphabetic writing for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Phonetic_alphabetic_writingUpdate(PermissionRequiredMixin, UpdateView):
    model = Phonetic_alphabetic_writing
    form_class = Phonetic_alphabetic_writingForm
    template_name = "sc/phonetic_alphabetic_writing/phonetic_alphabetic_writing_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Phonetic Alphabetic Writing"

        return context

class Phonetic_alphabetic_writingDelete(PermissionRequiredMixin, DeleteView):
    model = Phonetic_alphabetic_writing
    success_url = reverse_lazy('phonetic_alphabetic_writings')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Phonetic_alphabetic_writingListView(generic.ListView):
    model = Phonetic_alphabetic_writing
    template_name = "sc/phonetic_alphabetic_writing/phonetic_alphabetic_writing_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('phonetic_alphabetic_writings')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Phonetic Alphabetic Writing"
        context["var_main_desc"] = "Talking about writing systems, this refers to the kind of script"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Writing Systems"
        context["inner_vars"] = {'phonetic_alphabetic_writing': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of phonetic alphabetic writing for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Phonetic_alphabetic_writingListViewAll(generic.ListView):
    model = Phonetic_alphabetic_writing
    template_name = "sc/phonetic_alphabetic_writing/phonetic_alphabetic_writing_list_all.html"

    def get_absolute_url(self):
        return reverse('phonetic_alphabetic_writings_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Phonetic_alphabetic_writing.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Phonetic Alphabetic Writing"
        context["var_main_desc"] = "Talking about writing systems, this refers to the kind of script"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Writing Systems"
        context["inner_vars"] = {'phonetic_alphabetic_writing': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of phonetic alphabetic writing for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Phonetic_alphabetic_writingDetailView(generic.DetailView):
    model = Phonetic_alphabetic_writing
    template_name = "sc/phonetic_alphabetic_writing/phonetic_alphabetic_writing_detail.html"


@permission_required('admin.can_add_log_entry')
def phonetic_alphabetic_writing_download(request):
    items = Phonetic_alphabetic_writing.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="phonetic_alphabetic_writings.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'phonetic_alphabetic_writing', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.phonetic_alphabetic_writing, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def phonetic_alphabetic_writing_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="phonetic_alphabetic_writings.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Writing Systems, this refers to the kind of script', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Writing Systems'}
    my_meta_data_dic_inner_vars = {'phonetic_alphabetic_writing': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of phonetic alphabetic writing for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Lists_tables_and_classificationCreate(PermissionRequiredMixin, CreateView):
    model = Lists_tables_and_classification
    form_class = Lists_tables_and_classificationForm
    template_name = "sc/lists_tables_and_classification/lists_tables_and_classification_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('lists_tables_and_classification-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Lists Tables and Classification"
        context["my_exp"] = "Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'lists_tables_and_classification': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of lists tables and classification for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Lists_tables_and_classificationUpdate(PermissionRequiredMixin, UpdateView):
    model = Lists_tables_and_classification
    form_class = Lists_tables_and_classificationForm
    template_name = "sc/lists_tables_and_classification/lists_tables_and_classification_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Lists Tables and Classification"

        return context

class Lists_tables_and_classificationDelete(PermissionRequiredMixin, DeleteView):
    model = Lists_tables_and_classification
    success_url = reverse_lazy('lists_tables_and_classifications')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Lists_tables_and_classificationListView(generic.ListView):
    model = Lists_tables_and_classification
    template_name = "sc/lists_tables_and_classification/lists_tables_and_classification_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('lists_tables_and_classifications')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Lists Tables and Classification"
        context["var_main_desc"] = "Talking about kinds of written documents, no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'lists_tables_and_classification': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of lists tables and classification for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Lists_tables_and_classificationListViewAll(generic.ListView):
    model = Lists_tables_and_classification
    template_name = "sc/lists_tables_and_classification/lists_tables_and_classification_list_all.html"

    def get_absolute_url(self):
        return reverse('lists_tables_and_classifications_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Lists_tables_and_classification.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Lists Tables and Classification"
        context["var_main_desc"] = "Talking about kinds of written documents, no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'lists_tables_and_classification': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of lists tables and classification for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Lists_tables_and_classificationDetailView(generic.DetailView):
    model = Lists_tables_and_classification
    template_name = "sc/lists_tables_and_classification/lists_tables_and_classification_detail.html"


@permission_required('admin.can_add_log_entry')
def lists_tables_and_classification_download(request):
    items = Lists_tables_and_classification.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="lists_tables_and_classifications.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'lists_tables_and_classification', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.lists_tables_and_classification, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def lists_tables_and_classification_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="lists_tables_and_classifications.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Kinds of Written Documents'}
    my_meta_data_dic_inner_vars = {'lists_tables_and_classification': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of lists tables and classification for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class CalendarCreate(PermissionRequiredMixin, CreateView):
    model = Calendar
    form_class = CalendarForm
    template_name = "sc/calendar/calendar_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('calendar-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Calendar"
        context["my_exp"] = "Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'calendar': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of calendar for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class CalendarUpdate(PermissionRequiredMixin, UpdateView):
    model = Calendar
    form_class = CalendarForm
    template_name = "sc/calendar/calendar_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Calendar"

        return context

class CalendarDelete(PermissionRequiredMixin, DeleteView):
    model = Calendar
    success_url = reverse_lazy('calendars')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class CalendarListView(generic.ListView):
    model = Calendar
    template_name = "sc/calendar/calendar_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('calendars')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Calendar"
        context["var_main_desc"] = "Talking about kinds of written documents, no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'calendar': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of calendar for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class CalendarListViewAll(generic.ListView):
    model = Calendar
    template_name = "sc/calendar/calendar_list_all.html"

    def get_absolute_url(self):
        return reverse('calendars_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Calendar.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Calendar"
        context["var_main_desc"] = "Talking about kinds of written documents, no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'calendar': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of calendar for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class CalendarDetailView(generic.DetailView):
    model = Calendar
    template_name = "sc/calendar/calendar_detail.html"


@permission_required('admin.can_add_log_entry')
def calendar_download(request):
    items = Calendar.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="calendars.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'calendar', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.calendar, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def calendar_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="calendars.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Kinds of Written Documents'}
    my_meta_data_dic_inner_vars = {'calendar': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of calendar for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Sacred_textCreate(PermissionRequiredMixin, CreateView):
    model = Sacred_text
    form_class = Sacred_textForm
    template_name = "sc/sacred_text/sacred_text_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('sacred_text-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Sacred Text"
        context["my_exp"] = "Talking about Kinds of Written Documents, Sacred Texts originate from supernatural agents (deities), or are directly inspired by them."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'sacred_text': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of sacred text for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Sacred_textUpdate(PermissionRequiredMixin, UpdateView):
    model = Sacred_text
    form_class = Sacred_textForm
    template_name = "sc/sacred_text/sacred_text_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Sacred Text"

        return context

class Sacred_textDelete(PermissionRequiredMixin, DeleteView):
    model = Sacred_text
    success_url = reverse_lazy('sacred_texts')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Sacred_textListView(generic.ListView):
    model = Sacred_text
    template_name = "sc/sacred_text/sacred_text_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('sacred_texts')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Sacred Text"
        context["var_main_desc"] = "Talking about kinds of written documents, sacred texts originate from supernatural agents (deities), or are directly inspired by them."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'sacred_text': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of sacred text for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Sacred_textListViewAll(generic.ListView):
    model = Sacred_text
    template_name = "sc/sacred_text/sacred_text_list_all.html"

    def get_absolute_url(self):
        return reverse('sacred_texts_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Sacred_text.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Sacred Text"
        context["var_main_desc"] = "Talking about kinds of written documents, sacred texts originate from supernatural agents (deities), or are directly inspired by them."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'sacred_text': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of sacred text for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Sacred_textDetailView(generic.DetailView):
    model = Sacred_text
    template_name = "sc/sacred_text/sacred_text_detail.html"


@permission_required('admin.can_add_log_entry')
def sacred_text_download(request):
    items = Sacred_text.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sacred_texts.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'sacred_text', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.sacred_text, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def sacred_text_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sacred_texts.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Kinds of Written Documents, Sacred Texts originate from supernatural agents (deities), or are directly inspired by them.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Kinds of Written Documents'}
    my_meta_data_dic_inner_vars = {'sacred_text': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of sacred text for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Religious_literatureCreate(PermissionRequiredMixin, CreateView):
    model = Religious_literature
    form_class = Religious_literatureForm
    template_name = "sc/religious_literature/religious_literature_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('religious_literature-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Religious Literature"
        context["my_exp"] = "Talking about Kinds of Written Documents, Religious literature differs from the sacred texts. For example, it may provide commentary on the sacred texts, or advice on how to live a virtuous life."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'religious_literature': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of religious literature for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Religious_literatureUpdate(PermissionRequiredMixin, UpdateView):
    model = Religious_literature
    form_class = Religious_literatureForm
    template_name = "sc/religious_literature/religious_literature_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Religious Literature"

        return context

class Religious_literatureDelete(PermissionRequiredMixin, DeleteView):
    model = Religious_literature
    success_url = reverse_lazy('religious_literatures')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Religious_literatureListView(generic.ListView):
    model = Religious_literature
    template_name = "sc/religious_literature/religious_literature_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('religious_literatures')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Religious Literature"
        context["var_main_desc"] = "Talking about kinds of written documents, religious literature differs from the sacred texts. for example, it may provide commentary on the sacred texts, or advice on how to live a virtuous life."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'religious_literature': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of religious literature for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Religious_literatureListViewAll(generic.ListView):
    model = Religious_literature
    template_name = "sc/religious_literature/religious_literature_list_all.html"

    def get_absolute_url(self):
        return reverse('religious_literatures_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Religious_literature.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Religious Literature"
        context["var_main_desc"] = "Talking about kinds of written documents, religious literature differs from the sacred texts. for example, it may provide commentary on the sacred texts, or advice on how to live a virtuous life."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'religious_literature': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of religious literature for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Religious_literatureDetailView(generic.DetailView):
    model = Religious_literature
    template_name = "sc/religious_literature/religious_literature_detail.html"


@permission_required('admin.can_add_log_entry')
def religious_literature_download(request):
    items = Religious_literature.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="religious_literatures.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'religious_literature', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.religious_literature, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def religious_literature_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="religious_literatures.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Kinds of Written Documents, Religious literature differs from the sacred texts. For example, it may provide commentary on the sacred texts, or advice on how to live a virtuous life.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Kinds of Written Documents'}
    my_meta_data_dic_inner_vars = {'religious_literature': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of religious literature for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Practical_literatureCreate(PermissionRequiredMixin, CreateView):
    model = Practical_literature
    form_class = Practical_literatureForm
    template_name = "sc/practical_literature/practical_literature_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('practical_literature-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Practical Literature"
        context["my_exp"] = "Talking about Kinds of Written Documents, Practical literature refers to texts written with the aim of providing guidance on a certain topic, for example manuals on agriculture, warfare, or cooking. Letters do not count as practical literature."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'practical_literature': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of practical literature for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Practical_literatureUpdate(PermissionRequiredMixin, UpdateView):
    model = Practical_literature
    form_class = Practical_literatureForm
    template_name = "sc/practical_literature/practical_literature_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Practical Literature"

        return context

class Practical_literatureDelete(PermissionRequiredMixin, DeleteView):
    model = Practical_literature
    success_url = reverse_lazy('practical_literatures')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Practical_literatureListView(generic.ListView):
    model = Practical_literature
    template_name = "sc/practical_literature/practical_literature_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('practical_literatures')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Practical Literature"
        context["var_main_desc"] = "Talking about kinds of written documents, practical literature refers to texts written with the aim of providing guidance on a certain topic, for example manuals on agriculture, warfare, or cooking. letters do not count as practical literature."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'practical_literature': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of practical literature for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Practical_literatureListViewAll(generic.ListView):
    model = Practical_literature
    template_name = "sc/practical_literature/practical_literature_list_all.html"

    def get_absolute_url(self):
        return reverse('practical_literatures_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Practical_literature.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Practical Literature"
        context["var_main_desc"] = "Talking about kinds of written documents, practical literature refers to texts written with the aim of providing guidance on a certain topic, for example manuals on agriculture, warfare, or cooking. letters do not count as practical literature."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'practical_literature': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of practical literature for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Practical_literatureDetailView(generic.DetailView):
    model = Practical_literature
    template_name = "sc/practical_literature/practical_literature_detail.html"


@permission_required('admin.can_add_log_entry')
def practical_literature_download(request):
    items = Practical_literature.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="practical_literatures.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'practical_literature', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.practical_literature, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def practical_literature_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="practical_literatures.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Kinds of Written Documents, Practical literature refers to texts written with the aim of providing guidance on a certain topic, for example manuals on agriculture, warfare, or cooking. Letters do not count as practical literature.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Kinds of Written Documents'}
    my_meta_data_dic_inner_vars = {'practical_literature': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of practical literature for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class HistoryCreate(PermissionRequiredMixin, CreateView):
    model = History
    form_class = HistoryForm
    template_name = "sc/history/history_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('history-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "History"
        context["my_exp"] = "Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'history': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of history for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class HistoryUpdate(PermissionRequiredMixin, UpdateView):
    model = History
    form_class = HistoryForm
    template_name = "sc/history/history_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "History"

        return context

class HistoryDelete(PermissionRequiredMixin, DeleteView):
    model = History
    success_url = reverse_lazy('historys')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class HistoryListView(generic.ListView):
    model = History
    template_name = "sc/history/history_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('historys')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "History"
        context["var_main_desc"] = "Talking about kinds of written documents, no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'history': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of history for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class HistoryListViewAll(generic.ListView):
    model = History
    template_name = "sc/history/history_list_all.html"

    def get_absolute_url(self):
        return reverse('historys_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = History.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "History"
        context["var_main_desc"] = "Talking about kinds of written documents, no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'history': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of history for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class HistoryDetailView(generic.DetailView):
    model = History
    template_name = "sc/history/history_detail.html"


@permission_required('admin.can_add_log_entry')
def history_download(request):
    items = History.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="historys.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'history', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.history, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def history_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="historys.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Kinds of Written Documents'}
    my_meta_data_dic_inner_vars = {'history': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of history for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class PhilosophyCreate(PermissionRequiredMixin, CreateView):
    model = Philosophy
    form_class = PhilosophyForm
    template_name = "sc/philosophy/philosophy_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('philosophy-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Philosophy"
        context["my_exp"] = "Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'philosophy': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of philosophy for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class PhilosophyUpdate(PermissionRequiredMixin, UpdateView):
    model = Philosophy
    form_class = PhilosophyForm
    template_name = "sc/philosophy/philosophy_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Philosophy"

        return context

class PhilosophyDelete(PermissionRequiredMixin, DeleteView):
    model = Philosophy
    success_url = reverse_lazy('philosophys')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class PhilosophyListView(generic.ListView):
    model = Philosophy
    template_name = "sc/philosophy/philosophy_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('philosophys')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Philosophy"
        context["var_main_desc"] = "Talking about kinds of written documents, no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'philosophy': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of philosophy for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class PhilosophyListViewAll(generic.ListView):
    model = Philosophy
    template_name = "sc/philosophy/philosophy_list_all.html"

    def get_absolute_url(self):
        return reverse('philosophys_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Philosophy.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Philosophy"
        context["var_main_desc"] = "Talking about kinds of written documents, no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'philosophy': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of philosophy for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class PhilosophyDetailView(generic.DetailView):
    model = Philosophy
    template_name = "sc/philosophy/philosophy_detail.html"


@permission_required('admin.can_add_log_entry')
def philosophy_download(request):
    items = Philosophy.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="philosophys.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'philosophy', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.philosophy, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def philosophy_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="philosophys.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Kinds of Written Documents'}
    my_meta_data_dic_inner_vars = {'philosophy': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of philosophy for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Scientific_literatureCreate(PermissionRequiredMixin, CreateView):
    model = Scientific_literature
    form_class = Scientific_literatureForm
    template_name = "sc/scientific_literature/scientific_literature_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('scientific_literature-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Scientific Literature"
        context["my_exp"] = "Talking about Kinds of Written Documents, Scientific literature includes mathematics, natural sciences, social sciences"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'scientific_literature': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of scientific literature for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Scientific_literatureUpdate(PermissionRequiredMixin, UpdateView):
    model = Scientific_literature
    form_class = Scientific_literatureForm
    template_name = "sc/scientific_literature/scientific_literature_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Scientific Literature"

        return context

class Scientific_literatureDelete(PermissionRequiredMixin, DeleteView):
    model = Scientific_literature
    success_url = reverse_lazy('scientific_literatures')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Scientific_literatureListView(generic.ListView):
    model = Scientific_literature
    template_name = "sc/scientific_literature/scientific_literature_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('scientific_literatures')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Scientific Literature"
        context["var_main_desc"] = "Talking about kinds of written documents, scientific literature includes mathematics, natural sciences, social sciences"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'scientific_literature': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of scientific literature for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Scientific_literatureListViewAll(generic.ListView):
    model = Scientific_literature
    template_name = "sc/scientific_literature/scientific_literature_list_all.html"

    def get_absolute_url(self):
        return reverse('scientific_literatures_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Scientific_literature.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Scientific Literature"
        context["var_main_desc"] = "Talking about kinds of written documents, scientific literature includes mathematics, natural sciences, social sciences"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'scientific_literature': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of scientific literature for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Scientific_literatureDetailView(generic.DetailView):
    model = Scientific_literature
    template_name = "sc/scientific_literature/scientific_literature_detail.html"


@permission_required('admin.can_add_log_entry')
def scientific_literature_download(request):
    items = Scientific_literature.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="scientific_literatures.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'scientific_literature', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.scientific_literature, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def scientific_literature_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="scientific_literatures.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Kinds of Written Documents, Scientific literature includes mathematics, natural sciences, social sciences', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Kinds of Written Documents'}
    my_meta_data_dic_inner_vars = {'scientific_literature': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of scientific literature for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class FictionCreate(PermissionRequiredMixin, CreateView):
    model = Fiction
    form_class = FictionForm
    template_name = "sc/fiction/fiction_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('fiction-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Fiction"
        context["my_exp"] = "Talking about Kinds of Written Documents, fiction includes poetry."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'fiction': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of fiction for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class FictionUpdate(PermissionRequiredMixin, UpdateView):
    model = Fiction
    form_class = FictionForm
    template_name = "sc/fiction/fiction_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Fiction"

        return context

class FictionDelete(PermissionRequiredMixin, DeleteView):
    model = Fiction
    success_url = reverse_lazy('fictions')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class FictionListView(generic.ListView):
    model = Fiction
    template_name = "sc/fiction/fiction_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('fictions')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Fiction"
        context["var_main_desc"] = "Talking about kinds of written documents, fiction includes poetry."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'fiction': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of fiction for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class FictionListViewAll(generic.ListView):
    model = Fiction
    template_name = "sc/fiction/fiction_list_all.html"

    def get_absolute_url(self):
        return reverse('fictions_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Fiction.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Fiction"
        context["var_main_desc"] = "Talking about kinds of written documents, fiction includes poetry."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'fiction': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of fiction for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class FictionDetailView(generic.DetailView):
    model = Fiction
    template_name = "sc/fiction/fiction_detail.html"


@permission_required('admin.can_add_log_entry')
def fiction_download(request):
    items = Fiction.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="fictions.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'fiction', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.fiction, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def fiction_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="fictions.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Kinds of Written Documents, fiction includes poetry.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Kinds of Written Documents'}
    my_meta_data_dic_inner_vars = {'fiction': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of fiction for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class ArticleCreate(PermissionRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "sc/article/article_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('article-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Article"
        context["my_exp"] = "Talking about forms of money, articles are items that have both a regular use and are used as money (example: axes, cattle, measures of grain, ingots of non-precious metals)"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'article': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of article for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "sc/article/article_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Article"

        return context

class ArticleDelete(PermissionRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('articles')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class ArticleListView(generic.ListView):
    model = Article
    template_name = "sc/article/article_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('articles')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Article"
        context["var_main_desc"] = "Talking about forms of money, articles are items that have both a regular use and are used as money (example: axes, cattle, measures of grain, ingots of non-precious metals)"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Forms of money"
        context["inner_vars"] = {'article': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of article for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class ArticleListViewAll(generic.ListView):
    model = Article
    template_name = "sc/article/article_list_all.html"

    def get_absolute_url(self):
        return reverse('articles_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Article.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Article"
        context["var_main_desc"] = "Talking about forms of money, articles are items that have both a regular use and are used as money (example: axes, cattle, measures of grain, ingots of non-precious metals)"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Forms of money"
        context["inner_vars"] = {'article': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of article for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = "sc/article/article_detail.html"


@permission_required('admin.can_add_log_entry')
def article_download(request):
    items = Article.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="articles.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'article', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.article, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def article_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="articles.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about forms of money, articles are items that have both a regular use and are used as money (example: axes, cattle, measures of grain, ingots of non-precious metals)', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Forms of money'}
    my_meta_data_dic_inner_vars = {'article': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of article for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class TokenCreate(PermissionRequiredMixin, CreateView):
    model = Token
    form_class = TokenForm
    template_name = "sc/token/token_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('token-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Token"
        context["my_exp"] = "Talking about forms of money, tokens, unlike articles, are used only for exchange, and unlike coins, are not manufactured (example: cowries)"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'token': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of token for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class TokenUpdate(PermissionRequiredMixin, UpdateView):
    model = Token
    form_class = TokenForm
    template_name = "sc/token/token_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Token"

        return context

class TokenDelete(PermissionRequiredMixin, DeleteView):
    model = Token
    success_url = reverse_lazy('tokens')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class TokenListView(generic.ListView):
    model = Token
    template_name = "sc/token/token_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('tokens')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Token"
        context["var_main_desc"] = "Talking about forms of money, tokens, unlike articles, are used only for exchange, and unlike coins, are not manufactured (example: cowries)"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Forms of money"
        context["inner_vars"] = {'token': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of token for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class TokenListViewAll(generic.ListView):
    model = Token
    template_name = "sc/token/token_list_all.html"

    def get_absolute_url(self):
        return reverse('tokens_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Token.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Token"
        context["var_main_desc"] = "Talking about forms of money, tokens, unlike articles, are used only for exchange, and unlike coins, are not manufactured (example: cowries)"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Forms of money"
        context["inner_vars"] = {'token': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of token for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class TokenDetailView(generic.DetailView):
    model = Token
    template_name = "sc/token/token_detail.html"


@permission_required('admin.can_add_log_entry')
def token_download(request):
    items = Token.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tokens.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'token', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.token, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def token_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tokens.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about forms of money, tokens, unlike articles, are used only for exchange, and unlike coins, are not manufactured (example: cowries)', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Forms of money'}
    my_meta_data_dic_inner_vars = {'token': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of token for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Precious_metalCreate(PermissionRequiredMixin, CreateView):
    model = Precious_metal
    form_class = Precious_metalForm
    template_name = "sc/precious_metal/precious_metal_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('precious_metal-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Precious Metal"
        context["my_exp"] = "Talking about forms of money, Precious metals are non-coined silver, gold, platinum"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'precious_metal': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of precious metal for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Precious_metalUpdate(PermissionRequiredMixin, UpdateView):
    model = Precious_metal
    form_class = Precious_metalForm
    template_name = "sc/precious_metal/precious_metal_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Precious Metal"

        return context

class Precious_metalDelete(PermissionRequiredMixin, DeleteView):
    model = Precious_metal
    success_url = reverse_lazy('precious_metals')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Precious_metalListView(generic.ListView):
    model = Precious_metal
    template_name = "sc/precious_metal/precious_metal_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('precious_metals')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Precious Metal"
        context["var_main_desc"] = "Talking about forms of money, precious metals are non-coined silver, gold, platinum"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Forms of money"
        context["inner_vars"] = {'precious_metal': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of precious metal for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Precious_metalListViewAll(generic.ListView):
    model = Precious_metal
    template_name = "sc/precious_metal/precious_metal_list_all.html"

    def get_absolute_url(self):
        return reverse('precious_metals_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Precious_metal.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Precious Metal"
        context["var_main_desc"] = "Talking about forms of money, precious metals are non-coined silver, gold, platinum"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Forms of money"
        context["inner_vars"] = {'precious_metal': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of precious metal for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Precious_metalDetailView(generic.DetailView):
    model = Precious_metal
    template_name = "sc/precious_metal/precious_metal_detail.html"


@permission_required('admin.can_add_log_entry')
def precious_metal_download(request):
    items = Precious_metal.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="precious_metals.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'precious_metal', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.precious_metal, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def precious_metal_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="precious_metals.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about forms of money, Precious metals are non-coined silver, gold, platinum', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Forms of money'}
    my_meta_data_dic_inner_vars = {'precious_metal': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of precious metal for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Foreign_coinCreate(PermissionRequiredMixin, CreateView):
    model = Foreign_coin
    form_class = Foreign_coinForm
    template_name = "sc/foreign_coin/foreign_coin_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('foreign_coin-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Foreign Coin"
        context["my_exp"] = "NO_DESCRIPTIONS_IN_CODEBOOK"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'foreign_coin': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of foreign coin for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Foreign_coinUpdate(PermissionRequiredMixin, UpdateView):
    model = Foreign_coin
    form_class = Foreign_coinForm
    template_name = "sc/foreign_coin/foreign_coin_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Foreign Coin"

        return context

class Foreign_coinDelete(PermissionRequiredMixin, DeleteView):
    model = Foreign_coin
    success_url = reverse_lazy('foreign_coins')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Foreign_coinListView(generic.ListView):
    model = Foreign_coin
    template_name = "sc/foreign_coin/foreign_coin_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('foreign_coins')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Foreign Coin"
        context["var_main_desc"] = "NO Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Forms of money"
        context["inner_vars"] = {'foreign_coin': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of foreign coin for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Foreign_coinListViewAll(generic.ListView):
    model = Foreign_coin
    template_name = "sc/foreign_coin/foreign_coin_list_all.html"

    def get_absolute_url(self):
        return reverse('foreign_coins_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Foreign_coin.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Foreign Coin"
        context["var_main_desc"] = "NO Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Forms of money"
        context["inner_vars"] = {'foreign_coin': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of foreign coin for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Foreign_coinDetailView(generic.DetailView):
    model = Foreign_coin
    template_name = "sc/foreign_coin/foreign_coin_detail.html"


@permission_required('admin.can_add_log_entry')
def foreign_coin_download(request):
    items = Foreign_coin.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="foreign_coins.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'foreign_coin', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.foreign_coin, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def foreign_coin_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="foreign_coins.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'NO_DESCRIPTIONS_IN_CODEBOOK', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Forms of money'}
    my_meta_data_dic_inner_vars = {'foreign_coin': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of foreign coin for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Indigenous_coinCreate(PermissionRequiredMixin, CreateView):
    model = Indigenous_coin
    form_class = Indigenous_coinForm
    template_name = "sc/indigenous_coin/indigenous_coin_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('indigenous_coin-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Indigenous Coin"
        context["my_exp"] = "NO_DESCRIPTIONS_IN_CODEBOOK"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'indigenous_coin': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of indigenous coin for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Indigenous_coinUpdate(PermissionRequiredMixin, UpdateView):
    model = Indigenous_coin
    form_class = Indigenous_coinForm
    template_name = "sc/indigenous_coin/indigenous_coin_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Indigenous Coin"

        return context

class Indigenous_coinDelete(PermissionRequiredMixin, DeleteView):
    model = Indigenous_coin
    success_url = reverse_lazy('indigenous_coins')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Indigenous_coinListView(generic.ListView):
    model = Indigenous_coin
    template_name = "sc/indigenous_coin/indigenous_coin_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('indigenous_coins')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Indigenous Coin"
        context["var_main_desc"] = "NO Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Forms of money"
        context["inner_vars"] = {'indigenous_coin': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of indigenous coin for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Indigenous_coinListViewAll(generic.ListView):
    model = Indigenous_coin
    template_name = "sc/indigenous_coin/indigenous_coin_list_all.html"

    def get_absolute_url(self):
        return reverse('indigenous_coins_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Indigenous_coin.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Indigenous Coin"
        context["var_main_desc"] = "NO Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Forms of money"
        context["inner_vars"] = {'indigenous_coin': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of indigenous coin for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Indigenous_coinDetailView(generic.DetailView):
    model = Indigenous_coin
    template_name = "sc/indigenous_coin/indigenous_coin_detail.html"


@permission_required('admin.can_add_log_entry')
def indigenous_coin_download(request):
    items = Indigenous_coin.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="indigenous_coins.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'indigenous_coin', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.indigenous_coin, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def indigenous_coin_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="indigenous_coins.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'NO_DESCRIPTIONS_IN_CODEBOOK', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Forms of money'}
    my_meta_data_dic_inner_vars = {'indigenous_coin': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of indigenous coin for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Paper_currencyCreate(PermissionRequiredMixin, CreateView):
    model = Paper_currency
    form_class = Paper_currencyForm
    template_name = "sc/paper_currency/paper_currency_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('paper_currency-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Paper Currency"
        context["my_exp"] = "Paper currency or another kind of fiat money. Note that this only refers to indigenously produced paper currency. Code absent if colonial money is used."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'paper_currency': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of paper currency for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Paper_currencyUpdate(PermissionRequiredMixin, UpdateView):
    model = Paper_currency
    form_class = Paper_currencyForm
    template_name = "sc/paper_currency/paper_currency_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Paper Currency"

        return context

class Paper_currencyDelete(PermissionRequiredMixin, DeleteView):
    model = Paper_currency
    success_url = reverse_lazy('paper_currencys')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Paper_currencyListView(generic.ListView):
    model = Paper_currency
    template_name = "sc/paper_currency/paper_currency_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('paper_currencys')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Paper Currency"
        context["var_main_desc"] = "Paper currency or another kind of fiat money. note that this only refers to indigenously produced paper currency. code absent if colonial money is used."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Forms of money"
        context["inner_vars"] = {'paper_currency': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of paper currency for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Paper_currencyListViewAll(generic.ListView):
    model = Paper_currency
    template_name = "sc/paper_currency/paper_currency_list_all.html"

    def get_absolute_url(self):
        return reverse('paper_currencys_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Paper_currency.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Paper Currency"
        context["var_main_desc"] = "Paper currency or another kind of fiat money. note that this only refers to indigenously produced paper currency. code absent if colonial money is used."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Forms of money"
        context["inner_vars"] = {'paper_currency': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of paper currency for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Paper_currencyDetailView(generic.DetailView):
    model = Paper_currency
    template_name = "sc/paper_currency/paper_currency_detail.html"


@permission_required('admin.can_add_log_entry')
def paper_currency_download(request):
    items = Paper_currency.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="paper_currencys.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'paper_currency', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.paper_currency, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def paper_currency_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="paper_currencys.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Paper currency or another kind of fiat money. Note that this only refers to indigenously produced paper currency. Code absent if colonial money is used.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Forms of money'}
    my_meta_data_dic_inner_vars = {'paper_currency': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of paper currency for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class CourierCreate(PermissionRequiredMixin, CreateView):
    model = Courier
    form_class = CourierForm
    template_name = "sc/courier/courier_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('courier-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Courier"
        context["my_exp"] = "Full-time professional couriers."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'courier': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of courier for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class CourierUpdate(PermissionRequiredMixin, UpdateView):
    model = Courier
    form_class = CourierForm
    template_name = "sc/courier/courier_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Courier"

        return context

class CourierDelete(PermissionRequiredMixin, DeleteView):
    model = Courier
    success_url = reverse_lazy('couriers')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class CourierListView(generic.ListView):
    model = Courier
    template_name = "sc/courier/courier_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('couriers')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Courier"
        context["var_main_desc"] = "Full-time professional couriers."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Postal sytems"
        context["inner_vars"] = {'courier': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of courier for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class CourierListViewAll(generic.ListView):
    model = Courier
    template_name = "sc/courier/courier_list_all.html"

    def get_absolute_url(self):
        return reverse('couriers_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Courier.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Courier"
        context["var_main_desc"] = "Full-time professional couriers."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Postal sytems"
        context["inner_vars"] = {'courier': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of courier for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class CourierDetailView(generic.DetailView):
    model = Courier
    template_name = "sc/courier/courier_detail.html"


@permission_required('admin.can_add_log_entry')
def courier_download(request):
    items = Courier.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="couriers.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'courier', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.courier, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def courier_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="couriers.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Full-time professional couriers.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Postal sytems'}
    my_meta_data_dic_inner_vars = {'courier': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of courier for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Postal_stationCreate(PermissionRequiredMixin, CreateView):
    model = Postal_station
    form_class = Postal_stationForm
    template_name = "sc/postal_station/postal_station_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('postal_station-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Postal Station"
        context["my_exp"] = "Talking about postal sytems, Postal stations are specialized buildings exclusively devoted to the postal service. If there is a special building that has other functions than a postal station, we still code postal station as present. The intent is to capture additional infrastructure beyond having a corps of messengers."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'postal_station': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of postal station for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Postal_stationUpdate(PermissionRequiredMixin, UpdateView):
    model = Postal_station
    form_class = Postal_stationForm
    template_name = "sc/postal_station/postal_station_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Postal Station"

        return context

class Postal_stationDelete(PermissionRequiredMixin, DeleteView):
    model = Postal_station
    success_url = reverse_lazy('postal_stations')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Postal_stationListView(generic.ListView):
    model = Postal_station
    template_name = "sc/postal_station/postal_station_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('postal_stations')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Postal Station"
        context["var_main_desc"] = "Talking about postal sytems, postal stations are specialized buildings exclusively devoted to the postal service. if there is a special building that has other functions than a postal station, we still code postal station as present. the intent is to capture additional infrastructure beyond having a corps of messengers."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Postal sytems"
        context["inner_vars"] = {'postal_station': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of postal station for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Postal_stationListViewAll(generic.ListView):
    model = Postal_station
    template_name = "sc/postal_station/postal_station_list_all.html"

    def get_absolute_url(self):
        return reverse('postal_stations_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Postal_station.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Postal Station"
        context["var_main_desc"] = "Talking about postal sytems, postal stations are specialized buildings exclusively devoted to the postal service. if there is a special building that has other functions than a postal station, we still code postal station as present. the intent is to capture additional infrastructure beyond having a corps of messengers."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Postal sytems"
        context["inner_vars"] = {'postal_station': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of postal station for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Postal_stationDetailView(generic.DetailView):
    model = Postal_station
    template_name = "sc/postal_station/postal_station_detail.html"


@permission_required('admin.can_add_log_entry')
def postal_station_download(request):
    items = Postal_station.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="postal_stations.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'postal_station', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.postal_station, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def postal_station_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="postal_stations.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about postal sytems, Postal stations are specialized buildings exclusively devoted to the postal service. If there is a special building that has other functions than a postal station, we still code postal station as present. The intent is to capture additional infrastructure beyond having a corps of messengers.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Postal sytems'}
    my_meta_data_dic_inner_vars = {'postal_station': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of postal station for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class General_postal_serviceCreate(PermissionRequiredMixin, CreateView):
    model = General_postal_service
    form_class = General_postal_serviceForm
    template_name = "sc/general_postal_service/general_postal_service_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('general_postal_service-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "General Postal Service"
        context["my_exp"] = "Talking about postal sytems, 'General postal service' refers to a postal service that not only serves the ruler's needs, but carries mail for private citizens."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'general_postal_service': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of general postal service for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class General_postal_serviceUpdate(PermissionRequiredMixin, UpdateView):
    model = General_postal_service
    form_class = General_postal_serviceForm
    template_name = "sc/general_postal_service/general_postal_service_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "General Postal Service"

        return context

class General_postal_serviceDelete(PermissionRequiredMixin, DeleteView):
    model = General_postal_service
    success_url = reverse_lazy('general_postal_services')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class General_postal_serviceListView(generic.ListView):
    model = General_postal_service
    template_name = "sc/general_postal_service/general_postal_service_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('general_postal_services')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "General Postal Service"
        context["var_main_desc"] = "Talking about postal sytems, 'general postal service' refers to a postal service that not only serves the ruler's needs, but carries mail for private citizens."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Postal sytems"
        context["inner_vars"] = {'general_postal_service': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of general postal service for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class General_postal_serviceListViewAll(generic.ListView):
    model = General_postal_service
    template_name = "sc/general_postal_service/general_postal_service_list_all.html"

    def get_absolute_url(self):
        return reverse('general_postal_services_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = General_postal_service.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "General Postal Service"
        context["var_main_desc"] = "Talking about postal sytems, 'general postal service' refers to a postal service that not only serves the ruler's needs, but carries mail for private citizens."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Postal sytems"
        context["inner_vars"] = {'general_postal_service': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of general postal service for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class General_postal_serviceDetailView(generic.DetailView):
    model = General_postal_service
    template_name = "sc/general_postal_service/general_postal_service_detail.html"


@permission_required('admin.can_add_log_entry')
def general_postal_service_download(request):
    items = General_postal_service.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="general_postal_services.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'general_postal_service', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.general_postal_service, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('admin.can_add_log_entry')
def general_postal_service_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="general_postal_services.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': "Talking about postal sytems, 'General postal service' refers to a postal service that not only serves the ruler's needs, but carries mail for private citizens.", 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Postal sytems'}
    my_meta_data_dic_inner_vars = {'general_postal_service': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of general postal service for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

def scvars(request):
    my_sections_dic = {'Social Complexity Variables': {'staff': [['ra', 'ras', 'ra-create', 'ra-download', 'ra-metadownload', 'ras_all']], 'Social Scale': [['Polity Territory', 'polity_territorys', 'polity_territory-create', 'polity_territory-download', 'polity_territory-metadownload', 'polity_territorys_all'], ['Polity Population', 'polity_populations', 'polity_population-create', 'polity_population-download', 'polity_population-metadownload', 'polity_populations_all'], ['Population of the Largest Settlement', 'population_of_the_largest_settlements', 'population_of_the_largest_settlement-create', 'population_of_the_largest_settlement-download', 'population_of_the_largest_settlement-metadownload', 'population_of_the_largest_settlements_all']], 'Hierarchical Complexity': [['Settlement Hierarchy', 'settlement_hierarchys', 'settlement_hierarchy-create', 'settlement_hierarchy-download', 'settlement_hierarchy-metadownload', 'settlement_hierarchys_all'], ['Administrative Level', 'administrative_levels', 'administrative_level-create', 'administrative_level-download', 'administrative_level-metadownload', 'administrative_levels_all'], ['Religious Level', 'religious_levels', 'religious_level-create', 'religious_level-download', 'religious_level-metadownload', 'religious_levels_all'], ['Military Level', 'military_levels', 'military_level-create', 'military_level-download', 'military_level-metadownload', 'military_levels_all']], 'Professions': [['Professional Military Officer', 'professional_military_officers', 'professional_military_officer-create', 'professional_military_officer-download', 'professional_military_officer-metadownload', 'professional_military_officers_all'], ['Professional Soldier', 'professional_soldiers', 'professional_soldier-create', 'professional_soldier-download', 'professional_soldier-metadownload', 'professional_soldiers_all'], ['Professional Priesthood', 'professional_priesthoods', 'professional_priesthood-create', 'professional_priesthood-download', 'professional_priesthood-metadownload', 'professional_priesthoods_all']], 'Bureaucracy characteristics': [['Full Time Bureaucrat', 'full_time_bureaucrats', 'full_time_bureaucrat-create', 'full_time_bureaucrat-download', 'full_time_bureaucrat-metadownload', 'full_time_bureaucrats_all'], ['Examination System', 'examination_systems', 'examination_system-create', 'examination_system-download', 'examination_system-metadownload', 'examination_systems_all'], ['Merit Promotion', 'merit_promotions', 'merit_promotion-create', 'merit_promotion-download', 'merit_promotion-metadownload', 'merit_promotions_all'], ['Specialized Government Building', 'specialized_government_buildings', 'specialized_government_building-create', 'specialized_government_building-download', 'specialized_government_building-metadownload', 'specialized_government_buildings_all']], 'Law': [['Formal Legal Code', 'formal_legal_codes', 'formal_legal_code-create', 'formal_legal_code-download', 'formal_legal_code-metadownload', 'formal_legal_codes_all'], ['Judge', 'judges', 'judge-create', 'judge-download', 'judge-metadownload', 'judges_all'], ['Court', 'courts', 'court-create', 'court-download', 'court-metadownload', 'courts_all'], ['Professional Lawyer', 'professional_lawyers', 'professional_lawyer-create', 'professional_lawyer-download', 'professional_lawyer-metadownload', 'professional_lawyers_all']], 'Specialized Buildings': [['Irrigation System', 'irrigation_systems', 'irrigation_system-create', 'irrigation_system-download', 'irrigation_system-metadownload', 'irrigation_systems_all'], ['Drinking Water Supply System', 'drinking_water_supply_systems', 'drinking_water_supply_system-create', 'drinking_water_supply_system-download', 'drinking_water_supply_system-metadownload', 'drinking_water_supply_systems_all'], ['Market', 'markets', 'market-create', 'market-download', 'market-metadownload', 'markets_all'], ['Food Storage Site', 'food_storage_sites', 'food_storage_site-create', 'food_storage_site-download', 'food_storage_site-metadownload', 'food_storage_sites_all']], 'Transport infrastructure': [['Road', 'roads', 'road-create', 'road-download', 'road-metadownload', 'roads_all'], ['Bridge', 'bridges', 'bridge-create', 'bridge-download', 'bridge-metadownload', 'bridges_all'], ['Canal', 'canals', 'canal-create', 'canal-download', 'canal-metadownload', 'canals_all'], ['Port', 'ports', 'port-create', 'port-download', 'port-metadownload', 'ports_all']], 'Special purpose sites': [['Mines or Quarry', 'mines_or_quarrys', 'mines_or_quarry-create', 'mines_or_quarry-download', 'mines_or_quarry-metadownload', 'mines_or_quarrys_all']], 'Writing Systems': [['Mnemonic Device', 'mnemonic_devices', 'mnemonic_device-create', 'mnemonic_device-download', 'mnemonic_device-metadownload', 'mnemonic_devices_all'], ['Nonwritten Record', 'nonwritten_records', 'nonwritten_record-create', 'nonwritten_record-download', 'nonwritten_record-metadownload', 'nonwritten_records_all'], ['Written Record', 'written_records', 'written_record-create', 'written_record-download', 'written_record-metadownload', 'written_records_all'], ['Script', 'scripts', 'script-create', 'script-download', 'script-metadownload', 'scripts_all'], ['Non Phonetic Writing', 'non_phonetic_writings', 'non_phonetic_writing-create', 'non_phonetic_writing-download', 'non_phonetic_writing-metadownload', 'non_phonetic_writings_all'], ['Phonetic Alphabetic Writing', 'phonetic_alphabetic_writings', 'phonetic_alphabetic_writing-create', 'phonetic_alphabetic_writing-download', 'phonetic_alphabetic_writing-metadownload', 'phonetic_alphabetic_writings_all']], 'Kinds of Written Documents': [['Lists Tables and Classification', 'lists_tables_and_classifications', 'lists_tables_and_classification-create', 'lists_tables_and_classification-download', 'lists_tables_and_classification-metadownload', 'lists_tables_and_classifications_all'], ['Calendar', 'calendars', 'calendar-create', 'calendar-download', 'calendar-metadownload', 'calendars_all'], ['Sacred Text', 'sacred_texts', 'sacred_text-create', 'sacred_text-download', 'sacred_text-metadownload', 'sacred_texts_all'], ['Religious Literature', 'religious_literatures', 'religious_literature-create', 'religious_literature-download', 'religious_literature-metadownload', 'religious_literatures_all'], ['Practical Literature', 'practical_literatures', 'practical_literature-create', 'practical_literature-download', 'practical_literature-metadownload', 'practical_literatures_all'], ['History', 'historys', 'history-create', 'history-download', 'history-metadownload', 'historys_all'], ['Philosophy', 'philosophys', 'philosophy-create', 'philosophy-download', 'philosophy-metadownload', 'philosophys_all'], ['Scientific Literature', 'scientific_literatures', 'scientific_literature-create', 'scientific_literature-download', 'scientific_literature-metadownload', 'scientific_literatures_all'], ['Fiction', 'fictions', 'fiction-create', 'fiction-download', 'fiction-metadownload', 'fictions_all']], 'Forms of money': [['Article', 'articles', 'article-create', 'article-download', 'article-metadownload', 'articles_all'], ['Token', 'tokens', 'token-create', 'token-download', 'token-metadownload', 'tokens_all'], ['Precious Metal', 'precious_metals', 'precious_metal-create', 'precious_metal-download', 'precious_metal-metadownload', 'precious_metals_all'], ['Foreign Coin', 'foreign_coins', 'foreign_coin-create', 'foreign_coin-download', 'foreign_coin-metadownload', 'foreign_coins_all'], ['Indigenous Coin', 'indigenous_coins', 'indigenous_coin-create', 'indigenous_coin-download', 'indigenous_coin-metadownload', 'indigenous_coins_all'], ['Paper Currency', 'paper_currencys', 'paper_currency-create', 'paper_currency-download', 'paper_currency-metadownload', 'paper_currencys_all']], 'Postal sytems': [['Courier', 'couriers', 'courier-create', 'courier-download', 'courier-metadownload', 'couriers_all'], ['Postal Station', 'postal_stations', 'postal_station-create', 'postal_station-download', 'postal_station-metadownload', 'postal_stations_all'], ['General Postal Service', 'general_postal_services', 'general_postal_service-create', 'general_postal_service-download', 'general_postal_service-metadownload', 'general_postal_services_all']]}}
    context = {}
    context["my_dict"] = my_sections_dic
    return render(request, 'sc/scvars.html', context=context)

    