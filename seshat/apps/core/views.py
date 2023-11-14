from seshat.utils.utils import adder, dic_of_all_vars, list_of_all_Polities, dic_of_all_vars_in_sections

from django.contrib.sites.shortcuts import get_current_site
from seshat.apps.core.forms import SignUpForm, VariablehierarchyFormNew, CitationForm, ReferenceForm, SeshatCommentForm, SeshatCommentPartForm, PolityForm, CapitalForm, NgaForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db import IntegrityError, connection
from django.db.models import Prefetch, F, Value
from django.db.models.functions import Replace

from django.views.decorators.http import require_GET

from django.contrib.auth.decorators import login_required, permission_required
from seshat.apps.accounts.models import Seshat_Expert

from django.core.paginator import Paginator

from django.http import FileResponse
from django.shortcuts import get_object_or_404
import os



from markupsafe import Markup, escape
from django.http import JsonResponse

from django.core.mail import EmailMessage
import html
import csv

import json
from django.views import generic
from django.urls import reverse, reverse_lazy

from django.contrib.messages.views import SuccessMessageMixin

from ..general.models import Polity_research_assistant

from .models import Citation, Polity, Section, Subsection, Variablehierarchy, Reference, SeshatComment, SeshatCommentPart, Nga, Ngapolityrel, Capital, MacrostateShapefile, GADMShapefile
import pprint
import requests
from requests.structures import CaseInsensitiveDict
from seshat.utils.utils import adder, dic_of_all_vars, list_of_all_Polities, dic_of_all_vars_in_sections, dic_of_all_vars_with_varhier, get_all_data_for_a_polity, polity_detail_data_collector, get_all_general_data_for_a_polity, get_all_sc_data_for_a_polity, get_all_wf_data_for_a_polity, get_all_crisis_cases_data_for_a_polity, get_all_power_transitions_data_for_a_polity


from django.shortcuts import HttpResponse

from math import floor, ceil
from django.contrib.gis.geos import GEOSGeometry

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def ajax_test(request):
    if is_ajax(request=request):
        message = "This is ajax"
    else:
        message = "Not ajax"
    return HttpResponse(message)

# importing formset_factory
from django.forms import formset_factory, modelformset_factory


def index(request):
    return HttpResponse('<h1>Hello World.</h1>')

def four_o_four(request):
    return render(request, 'core/not_found_404.html')

def seshatindex(request):
    context = {
        'insta': "Instabilities All Over the Place..",
        'trans': "Transitions All Over the Place",
    }
    #print('static_root:', settings.STATIC_ROOT)
    #print('STATICFILES_DIRS:', settings.STATICFILES_DIRS)
    return render(request, 'core/seshat-index.html', context=context)

def seshatmethods(request):
    context = {
        'insta': "Instabilities All Over the Place..",
        'trans': "Transitions All Over the Place",
    }
    #print('static_root:', settings.STATIC_ROOT)
    #print('STATICFILES_DIRS:', settings.STATICFILES_DIRS)
    return render(request, 'core/seshat-methods.html', context=context)

def seshatwhoweare(request):
    #json_url_inners = "https://eric.clst.org/assets/wiki/uploads/Stuff/gz_2010_us_040_00_500k.json"
    #json_url_outline = "https://eric.clst.org/assets/wiki/uploads/Stuff/gz_2010_us_outline_500k.json"
    json_file_path = "/home/majid/dev/seshat/seshat/seshat/apps/core/static/geojson/us_states_geojson.json"

    try:
        #response_inners = requests.get(json_url_inners)
        #response_outline = requests.get(json_url_outline)
        with open(json_file_path, "r") as json_file:
            json_data = json.load(json_file)
        #with open(json_file_path, "r") as json_file:
        #    json_data = json.load(json_file)
        # Check if the request was successful (status code 200)
        #if response_inners.status_code == 200 and response_outline.status_code == 200:
        #    # Parse the JSON data from the response_inners
        #    json_inners = response_inners.json()
        #    json_outline = response_outline.json()

        context = {
                'insta': "Instabilities All Over the Place..",
                'json_data': json_data,  # Add this line to your context
        }
        print(len(json_data))
        return render(request, 'core/seshat-whoweare.html', context=context)
    except FileNotFoundError:
        # Handle the case when the file is not found
        context = {
            'insta': "Instabilities All Over the Place..",
            'json_error': "JSON file not found",
        }
        return render(request, 'core/seshat-whoweare.html', context=context)
    except json.JSONDecodeError as e:
        # Handle JSON decoding errors if the file is not valid JSON
        context = {
            'insta': "Instabilities All Over the Place..",
            'json_error': f"JSON decoding error: {str(e)}",
        }
        return render(request, 'core/seshat-whoweare.html', context=context)

def seshatolddownloads(request):
    context = {
        'insta': "Instabilities All Over the Place..",
    }
    return render(request, 'core/old_downloads.html', context=context)

def seshatacknowledgements(request):
    context = {
        'insta': "Instabilities All Over the Place..",
    }
    return render(request, 'core/seshat-acknowledgements.html', context=context)

class ReferenceListView(generic.ListView):
    model = Reference
    template_name = "core/references/reference_list.html"
    paginate_by = 20

    def get_absolute_url(self):
        return reverse('references')

    def get_queryset(self):
        queryset = Reference.objects.exclude(creator='MAJIDBENAM').all()
        return queryset
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     selected_only_zotero_refs = Reference.objects.exclude(creator='MAJIDBENAM')
    #     context['object_list'] = selected_only_zotero_refs

    #     return context


class NlpReferenceListView(generic.ListView):
    model = Reference
    template_name = "core/references/nlp_reference_list.html"
    paginate_by = 50

    def get_absolute_url(self):
        return reverse('nlp-references')

    def get_queryset(self):
        # Import the list of Zotero links inside the method
        from .nlp_zotero_links import NLP_ZOTERO_LINKS_TO_FILTER

        # Use the imported list of Zotero links to filter references
        queryset = Reference.objects.filter(zotero_link__in=NLP_ZOTERO_LINKS_TO_FILTER)

        queryset = queryset.filter(year__gt=0)

        # Replace underscores in 'creator' with spaces
        queryset = queryset.annotate(
            creator_with_spaces=Replace('creator', Value('_'), Value(' '))
        )

        # Replace "_et_al" at the end of 'creator' with ", ..."
        queryset = queryset.annotate(
            creator_cleaned=Replace(F('creator_with_spaces'), Value(' et al'), Value(', ...'))
        )

        queryset = queryset.order_by('-year', 'title')

        # Create a list of Zotero links from the queryset
        #matched_zotero_links = list(queryset.values_list('zotero_link', flat=True))

        # Find the missing Zotero links
        #missing_zotero_links = [link for link in NLP_ZOTERO_LINKS_TO_FILTER if link not in matched_zotero_links]

        #print(missing_zotero_links)

        return queryset

# references without a Zotero link:
def no_zotero_refs_list(request):
    selected_no_zotero_refs = Reference.objects.filter(zotero_link__startswith='NOZOTERO_')
    #all_refs = Reference.objects.all()
    #selected_no_zotero_refs = []
    #for ref in all_refs:
    #    if "NOZOTERO_" in ref.zotero_link:
    #        selected_no_zotero_refs.append(ref)

    paginator = Paginator(selected_no_zotero_refs, 10) # Show 25 refs per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {}
    context['object_list'] = selected_no_zotero_refs
    context['page_obj'] = page_obj
    context['is_paginated'] = False


    # Citation.objects.bulk_create(all_citations)
    return render (request, 'core/references/reference_list_nozotero.html', context)

def reference_update_modal(request, pk):
    # Either render only the modal content, or a full standalone page
    if is_ajax(request=request):
        template_name = 'core/references/reference_update_modal.html'
    else:
        template_name = 'core/references/reference_update.html'

    object = Reference.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReferenceForm(instance=object, data=request.POST)
        if form.is_valid():
            form.save()
            if not is_ajax(request=request):
                # reload the page
                next = request.META['PATH_INFO']
                return HttpResponseRedirect(next)
            # if is_ajax(), we just return the validated form, so the modal will close
    else:
        form = ReferenceForm(instance=object)

    return render(request, template_name, {
        'object': object,
        'form': form,
    })

###########


class ReferenceCreate(PermissionRequiredMixin, CreateView):
    model = Reference
    form_class = ReferenceForm
    template_name = "core/references/reference_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('reference-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mysection"] = "xyz"
        context["mysubsection"] = "abc"
        context["myvar"] = "def reference"
        context["errors"] = "Halooooooooo"
        #print(context)

        return context

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponseRedirect(reverse('seshat-index'))


class ReferenceUpdate(PermissionRequiredMixin, UpdateView):
    model = Reference
    form_class = ReferenceForm
    template_name = "core/references/reference_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mysection"] = "Fiscal Heeeelath"
        context["mysubsection"] = "No Subsection Proeeeevided"
        context["myvar"] = "Reference Daeeeeta"

        return context

class ReferenceDelete(PermissionRequiredMixin, DeleteView):
    model = Reference
    success_url = reverse_lazy('references')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class ReferenceDetailView(generic.DetailView):
    model = Reference
    template_name = "core/references/reference_detail.html"



@permission_required('core.view_capital')
def references_download(request):
    items = Reference.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="referencess.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['zotero_link', 'creator'])

    for obj in items:
        writer.writerow([obj.zotero_link, obj.creator])

    return response


# Citations
class CitationListView(generic.ListView):
    model = Citation
    template_name = "core/references/citation_list.html"
    paginate_by = 20

    def get_absolute_url(self):
        return reverse('citations')

class CitationCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Citation
    form_class = CitationForm
    template_name = "core/references/citation_form.html"
    permission_required = 'core.add_capital'
    success_message = "Yoohoooo..."

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context.update({"my_message": "Soemthign went wrong"})
        return self.render_to_response(context)

    def get_absolute_url(self):
        return reverse('citation-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mysection"] = "xyz"
        context["mysubsection"] = "abc"
        context["myvar"] = "def citation"
        context["errors"] = "Halooooooooo"
        #print(context)

        return context

    def form_valid(self, form):
        return super().form_valid(form)
    
    # def form_invalid(self, form):
    #     return HttpResponseRedirect(reverse('seshat-index'))


class CitationUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Citation
    form_class = CitationForm
    template_name = "core/references/citation_update.html"
    permission_required = 'core.add_capital'
    success_message = "Yoohoooo..."

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context.update({"my_message": "Soemthign went wrong"})
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mysection"] = "Fiscal Helath"
        context["mysubsection"] = "No Subsection Provided"
        context["myvar"] = "Citation Data xyz"

        return context

class CitationDelete(PermissionRequiredMixin, DeleteView):
    model = Citation
    success_url = reverse_lazy('citations')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class CitationDetailView(generic.DetailView):
    model = Citation
    template_name = "core/references/citation_detail.html"

# SeshatComment
class SeshatCommentListView(generic.ListView):
    model = SeshatComment
    template_name = "core/seshatcomments/seshatcomment_list.html"
    paginate_by = 20

    def get_absolute_url(self):
        return reverse('seshatcomments')

class SeshatCommentCreate(PermissionRequiredMixin, CreateView):
    model = SeshatComment
    form_class = SeshatCommentForm
    template_name = "core/seshatcomments/seshatcomment_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('seshatcomment-create')


    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponseRedirect(reverse('seshat-index'))


class SeshatCommentUpdate(PermissionRequiredMixin, UpdateView):
    model = SeshatComment
    form_class = SeshatCommentForm
    template_name = "core/seshatcomments/seshatcomment_update.html"
    permission_required = 'core.add_capital'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     related_models = [model for model in dir(self.object) if '_related' in model]

    #     for model_name in related_models:
    #         print(model_name)
    #         related_objects = getattr(self.object, model_name)
    #         if related_objects:
    #             context['related_objects'] = related_objects
    #             break

    #     return context


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     #an_instance = SeshatComment.objects.first()
    #     #related_fact = 
    #     #print("Haloooooo_________ooooooooooo", self.kwargs['com_id'])
    #     #print("Halooooooooooooooooo", self.kwargs['subcom_order'])
    #     #related_fact = self.        context["com_id"] = self.kwargs['com_id']
    #     #context["subcom_order"] = self.kwargs['subcom_order']
    #     #context["subcom_order"] = self.comment_order

    #     print("HEre we gooooooooooo: ", dir(self.object))
    #     #for potential_attr in dir(isinstance):
            
    #     #if an_instance

    #     return context

class SeshatCommentDelete(PermissionRequiredMixin, DeleteView):
    model = SeshatComment
    success_url = reverse_lazy('seshatcomments')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class SeshatCommentDetailView(generic.DetailView):
    model = SeshatComment
    template_name = "core/seshatcomments/seshatcomment_detail.html"


# SeshatCommentPart
class SeshatCommentPartListView(generic.ListView):
    model = SeshatCommentPart
    template_name = "core/seshatcomments/seshatcommentpart_list.html"
    paginate_by = 20

    def get_absolute_url(self):
        return reverse('seshatcommentparts')

class SeshatCommentPartCreate(PermissionRequiredMixin, CreateView):
    model = SeshatCommentPart
    form_class = SeshatCommentPartForm
    template_name = "core/seshatcomments/seshatcommentpart_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('seshatcommentpart-create')


    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponseRedirect(reverse('seshat-index'))

class SeshatCommentPartCreate2(PermissionRequiredMixin, CreateView):
    model = SeshatCommentPart
    form_class = SeshatCommentPartForm
    template_name = "core/seshatcomments/seshatcommentpart_form_prefilled.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('seshatcommentpart-create2')


    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponseRedirect(reverse('seshat-index'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logged_in_user = self.request.user
        logged_in_expert = Seshat_Expert.objects.get(user=logged_in_user)
        #print("Haloooooo_________ooooooooooo", self.kwargs['com_id'])
        #print("Halooooooooooooooooo", self.kwargs['subcom_order'])
        context["com_id"] = self.kwargs['com_id']
        context["subcom_order"] = self.kwargs['subcom_order']
        context["comment_curator"] = logged_in_expert
        context["comment_curator_id"] = logged_in_expert.id
        context["comment_curator_name"] = "Selected USER"

        #context["subcom_order"] = self.comment_order

        #print(context)

        return context

class SeshatCommentPartUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SeshatCommentPart
    form_class = SeshatCommentPartForm
    template_name = "core/seshatcomments/seshatcommentpart_update.html"
    permission_required = 'core.add_capital'
    success_message = "You successfully updated the subdescription."


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logged_in_user = self.request.user
        logged_in_expert = Seshat_Expert.objects.get(user=logged_in_user)
        #context["com_id"] = self.kwargs['com_id']
        #context["subcom_order"] = self.kwargs['subcom_order']
        context["comment_curator"] = logged_in_expert
        context["comment_curator_id"] = logged_in_expert.id
        context["comment_curator_name"] = "Selected USER"

        #context["subcom_order"] = self.comment_order

        #print(context)

        return context


class SeshatCommentPartDelete(PermissionRequiredMixin, DeleteView):
    model = SeshatCommentPart
    success_url = reverse_lazy('seshatcommentparts')
    #success_url = reverse_lazy('seshatcommentparts')

    #('seshatcomment-update', self.pk)
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class SeshatCommentPartDetailView(generic.DetailView):
    model = SeshatCommentPart
    template_name = "core/seshatcomments/seshatcommentpart_detail.html"




##### Extra function for seshat comments


# POLITY

class PolityCreate(PermissionRequiredMixin, CreateView):
    model = Polity
    form_class = PolityForm
    template_name = "core/polity/polity_form.html"
    permission_required = 'core.add_capital'
    success_url = reverse_lazy('polities')

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponseRedirect(reverse('seshat-index'))


class PolityUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Polity
    form_class = PolityForm
    template_name = "core/polity/polity_form.html"
    permission_required = 'core.add_capital'
    success_message = "You successfully updated the Polity."
    
    def get_success_url(self):
        return reverse_lazy('polity-detail-main', kwargs={'pk': self.object.pk})
    #success_url = reverse_lazy('polity-detail-main')



# class PolityListView(PermissionRequiredMixin, SuccessMessageMixin, generic.ListView):
#     model = Polity
#     template_name = "core/polity/polity_list.html"
#     permission_required = 'core.add_capital'

#     def get_absolute_url(self):
#         return reverse('polities')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         all_ngas = Nga.objects.all()
#         all_pols = Polity.objects.select_related('ngapolityrel__polity_party', 'ngapolityrel__nga_party').order_by('start_year').all()
#         all_nga_pol_rels = Ngapolityrel.objects.all()

#         all_world_regions = {a_nga.world_region: [a_nga.subregion] for a_nga in all_ngas}

#         ultimate_wregion_dic = {}

#         for a_world_region, all_its_sub_regions in all_world_regions.items():
#             ultimate_wregion_dic[a_world_region] = {}

#             for a_subregion in all_its_sub_regions:
#                 all_politys_on_the_polity_list_page = Polity.objects.filter(
#                     ngapolityrel__polity_party__name=F('name'),
#                     ngapolityrel__nga_party__world_region=a_world_region,
#                     ngapolityrel__nga_party__subregion=a_subregion
#                 ).distinct()

#                 ultimate_wregion_dic[a_world_region][a_subregion] = list(all_politys_on_the_polity_list_page)

#         context["all_ngas"] = all_ngas
#         context["all_nga_pol_rels"] = all_nga_pol_rels
#         context["all_world_regions"] = all_world_regions
#         context["ultimate_wregion_dic"] = ultimate_wregion_dic

#         return context


class PolityListView_old(PermissionRequiredMixin, SuccessMessageMixin, generic.ListView):
    model = Polity
    template_name = "core/polity/polity_list.html"
    permission_required = 'core.add_capital'

    #paginate_by = 10

    def get_absolute_url(self):
        return reverse('polities')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_ngas = Nga.objects.all()
        all_pols = Polity.objects.all().order_by('start_year')
        all_nga_pol_rels  = Ngapolityrel.objects.all()
        all_world_regions = {}
        for a_nga in all_ngas:
            if a_nga.world_region not in all_world_regions.keys():
                all_world_regions[a_nga.world_region] = [a_nga.subregion]
            else:
                if a_nga.subregion not in all_world_regions[a_nga.world_region]:
                    all_world_regions[a_nga.world_region].append(a_nga.subregion)
        
        ultimate_wregion_dic = {'Europe': {},
        'Southwest Asia': {},
        'Africa':  {},
        'Central Eurasia': {},
        'South Asia':  {},
        'Southeast Asia': {},
        'East Asia':  {},
        'Oceania-Australia':  {},
        'North America':  {},
        'South America':  {},
        }
        all_politys_on_the_polity_list_page = []
        for a_world_region, all_its_sub_regions in all_world_regions.items():
            for a_subregion in all_its_sub_regions:
                list_for_a_subregion = []
                for a_polity in all_pols:
                    for a_rel in all_nga_pol_rels:
                        if a_rel.polity_party.name == a_polity.name and a_world_region == a_rel.nga_party.world_region and a_subregion == a_rel.nga_party.subregion and a_polity not in list_for_a_subregion:
                            list_for_a_subregion.append(a_polity)
                            if a_polity not in all_politys_on_the_polity_list_page:
                                all_politys_on_the_polity_list_page.append(a_polity)
                        
                ultimate_wregion_dic[a_world_region][a_subregion] = list_for_a_subregion
        context["all_ngas"] = all_ngas
        context["all_nga_pol_rels"] = all_nga_pol_rels
        context["all_world_regions"] = all_world_regions
        context["ultimate_wregion_dic"] = ultimate_wregion_dic
        #print(ultimate_wregion_dic)

        #print(f"out of {len(all_pols)}: {len(all_politys_on_the_polity_list_page)} were taken care of.")
        

        return context

class PolityListView1(SuccessMessageMixin, generic.ListView):
    model = Polity
    template_name = "core/polity/polity_list.html"

    #paginate_by = 10

    def get_absolute_url(self):
        return reverse('polities')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_ngas = Nga.objects.all()
        all_pols = Polity.objects.all().order_by('start_year')
        all_nga_pol_rels  = Ngapolityrel.objects.all()
        all_world_regions = {}
        for a_nga in all_ngas:
            if a_nga.world_region not in all_world_regions.keys():
                all_world_regions[a_nga.world_region] = [a_nga.subregion]
            else:
                if a_nga.subregion not in all_world_regions[a_nga.world_region]:
                    all_world_regions[a_nga.world_region].append(a_nga.subregion)
        
        ultimate_wregion_dic = {'Europe': {},
        'Southwest Asia': {},
        'Africa':  {},
        'Central Eurasia': {},
        'South Asia':  {},
        'Southeast Asia': {},
        'East Asia':  {},
        'Oceania-Australia':  {},
        'North America':  {},
        'South America':  {},
        'Nomad Polities': {
            "Nomad Land": []
        },
        }
        all_politys_on_the_polity_list_page = []
        nomad_polities = []
        for a_world_region, all_its_sub_regions in all_world_regions.items():
            for a_subregion in all_its_sub_regions:
                list_for_a_subregion = []
                for a_polity in all_pols:
                    for a_rel in all_nga_pol_rels:
                        if a_rel.polity_party.name == a_polity.name and a_world_region == a_rel.nga_party.world_region and a_subregion == a_rel.nga_party.subregion and a_polity not in list_for_a_subregion:
                            list_for_a_subregion.append(a_polity)
                            if a_polity not in all_politys_on_the_polity_list_page:
                                all_politys_on_the_polity_list_page.append(a_polity)
                        
                ultimate_wregion_dic[a_world_region][a_subregion] = list_for_a_subregion
        # nomads
        for a_polity in all_pols:
            if a_polity not in nomad_polities and a_polity not in all_politys_on_the_polity_list_page:
                nomad_polities.append(a_polity)
        ultimate_wregion_dic['Nomad Polities'][ "Nomad Land"] = nomad_polities
        context["all_ngas"] = all_ngas
        context["all_nga_pol_rels"] = all_nga_pol_rels
        context["all_world_regions"] = all_world_regions
        context["ultimate_wregion_dic"] = ultimate_wregion_dic
        #print(ultimate_wregion_dic)

        #print(f"out of {len(all_pols)}: {len(all_politys_on_the_polity_list_page)} were taken care of.")
        

        return context
    

class PolityListView(SuccessMessageMixin, generic.ListView):
    model = Polity
    template_name = "core/polity/polity_list.html"

    #paginate_by = 10

    def get_absolute_url(self):
        return reverse('polities')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_ngas = Nga.objects.all()
        all_pols = Polity.objects.all().order_by('start_year')
        #all_nga_pol_rels  = Ngapolityrel.objects.all()
        all_world_regions = {}
        for a_nga in all_ngas:
            if a_nga.world_region not in all_world_regions.keys():
                all_world_regions[a_nga.world_region] = [a_nga.subregion]
            else:
                if a_nga.subregion not in all_world_regions[a_nga.world_region]:
                    all_world_regions[a_nga.world_region].append(a_nga.subregion)
        
        ultimate_wregion_dic = {'Europe': {},
        'Southwest Asia': {},
        'Africa':  {},
        'Central Eurasia': {},
        'South Asia':  {},
        'Southeast Asia': {},
        'East Asia':  {},
        'Oceania-Australia':  {},
        'North America':  {},
        'South America':  {},
        'Nomad Polities': {
            "Nomad Land": []
        },
        }

        sub_regions_details = {'Western Europe': 'British Isles, France, Low Countries, Switzerland', 'Southern Europe': 'Iberia, Italy, Sicily, Sardinia, Corsica, Balearics', 'Northern Europe': 'Iceland, Scandinavia, Finland, Baltics, Karelia, Kola Peninsula', 'Central Europe': 'Germany, Poland, Austria, Hungary, Czechia, Slovakia', 'Southeastern Europe': 'Yugoslavia, Romania-Moldova, Bulgaria, Albania, Greece', 'Eastern Europe': 'Belarus, non-Steppe Russia and Ukraine', 'Maghreb': 'From Morocco to Libya', 'Northeastern Africa': 'Egypt and Sudan (the Nile Basin)', 'Sahel': 'Mauritania, Mali, Burkina Faso, Niger, Chad (Arid)', 'West Africa': 'From Senegal to Gabon (Tropical)', 'Central Africa': 'Angola and DRC', 'East Africa': 'Tanzania, Burundi, Uganda, So Sudan, Somalia, Ethiopia, Eritrea', 'Southern Africa': 'Namibia, Zambia, Malawi, Mozambique and south', 'Anatolia-Caucasus': 'Turkey, Armenia, Georgia, Azerbaijan', 'Levant-Mesopotamia': 'Israel, Jordan, Lebanon, Syria, Iraq, Kuwait, Khuzestan (Susiana)', 'Arabia': 'Arabian Peninsula', 'Iran': 'Persia, most of Afghanistan, (western Pakistan?)', 'Pontic-Caspian ': 'The steppe belt of Ukraine and Russia', 'Turkestan': 'Turkmenistan, Uzbekistan, Tajikistan, Kyrgyzstan, Kazakstan, Xinjiang', 'Afghanistan': 'Afghanistan', 'Mongolia': 'Mongolia, Inner Mongolia, the steppe part of Manchuria', 'Siberia': 'Urals, West Siberia, Central Siberia, Yakutia', 'Arctic Asia': 'The tundra and arctic regions of Eurasia sans Scandinavia', 'Tibet': 'Tibet', 'Northeast Asia': 'Korea, Japan, forest part of Manchuria, Russian Far East', 'China': 'China without Tibet, Inner Mongolia, and Xinjiang', 'Indo-Gangetic Plain': 'Pakistan, Punjab, upper and middle Ganges', 'Eastern India': 'Lower Ganges (Bangladesh) and eastern India (Assam)', 'Central India': 'Deccan, etc', 'Southern India': 'Southern India and Sri Lanka', 'Mainland': 'Myanmar, Thailand, Cambodia, Laos, south Vietnam', 'Archipelago': 'Malaysia, Indonesia, Philippines', 'Australia': 'Australia', 'New Guinea': 'New Guinea', 'Polynesia': 'Polynesia', 'Arctic America': 'Alaska, Arctic Canada, Greenland', 'Western NA': 'West Coast, the Rockies, and the American SouthWest', 'Great Plains': 'American Great Plains', 'Mississippi Basin': 'From the Great Lakes to Louisiana', 'East Coast': 'East Coast of US', 'Mexico': 'Mexico and Central America (without Panama)', 'Caribbean': 'Caribbean islands, Panama, coastal Columbia-Venezuela', 'Andes': 'From Ecuador to Chile', 'Amazonia': 'Brazil, Guyanas, plus Amazonian parts of bordering states', 'Southern Cone': 'Parguay, Uruguay, Argentina'}
        all_politys_on_the_polity_list_page = []
        nomad_polities = []

        # modify the world regions:
        all_world_regions["Africa"].append("East Africa")
        all_world_regions["Africa"].append("Southern Africa")
        all_world_regions["South Asia"].append("Southern India")


        for a_world_region, all_its_sub_regions in all_world_regions.items():
            for a_subregion in all_its_sub_regions:
                list_for_a_subregion = []
                extras_for_AFR_WEST = []
                extras_for_AFR_EAST = []
                extras_for_AFR_SA = []
                extras_for_SA_SI = []

                for a_polity in all_pols:
                    if a_polity.home_nga and a_world_region == a_polity.home_nga.world_region and a_subregion == a_polity.home_nga.subregion and a_polity not in list_for_a_subregion:
                        list_for_a_subregion.append(a_polity)
                        if a_polity not in all_politys_on_the_polity_list_page:
                            all_politys_on_the_polity_list_page.append(a_polity)
                    elif a_polity.polity_tag == "POL_AFR_WEST":
                        extras_for_AFR_WEST.append(a_polity)
                        if a_polity not in all_politys_on_the_polity_list_page:
                            all_politys_on_the_polity_list_page.append(a_polity)
                    elif a_polity.polity_tag == "POL_AFR_EAST":
                        extras_for_AFR_EAST.append(a_polity)
                        if a_polity not in all_politys_on_the_polity_list_page:
                            all_politys_on_the_polity_list_page.append(a_polity)
                    elif a_polity.polity_tag == "POL_AFR_SA":
                        extras_for_AFR_SA.append(a_polity)
                        if a_polity not in all_politys_on_the_polity_list_page:
                            all_politys_on_the_polity_list_page.append(a_polity)
                    elif a_polity.polity_tag == "POL_SA_SI":
                        extras_for_SA_SI.append(a_polity)
                        if a_polity not in all_politys_on_the_polity_list_page:
                            all_politys_on_the_polity_list_page.append(a_polity)

                if a_world_region == "Africa" and a_subregion == "West Africa":
                    ultimate_wregion_dic[a_world_region][a_subregion] = list_for_a_subregion + extras_for_AFR_WEST
                elif a_world_region == "Africa" and a_subregion == "East Africa":
                    ultimate_wregion_dic[a_world_region][a_subregion] = list_for_a_subregion + extras_for_AFR_EAST
                elif a_world_region == "Africa" and a_subregion == "Southern Africa":
                   ultimate_wregion_dic[a_world_region][a_subregion] = list_for_a_subregion + extras_for_AFR_SA
                elif a_world_region == "South Asia" and a_subregion == "Southern India":
                   ultimate_wregion_dic[a_world_region][a_subregion] = list_for_a_subregion + extras_for_SA_SI
                else:
                    ultimate_wregion_dic[a_world_region][a_subregion] = list_for_a_subregion

                        
        # nomads
        for a_polity in all_pols:
            if a_polity not in nomad_polities and a_polity not in all_politys_on_the_polity_list_page:
                nomad_polities.append(a_polity)
        ultimate_wregion_dic['Nomad Polities'][ "Nomad Land"] = nomad_polities
        context["sub_regions_details"] = sub_regions_details
        #context["all_nga_pol_rels"] = all_nga_pol_rels
        context["all_world_regions"] = all_world_regions
        context["ultimate_wregion_dic"] = ultimate_wregion_dic
        #print(ultimate_wregion_dic)

        #print(f"out of {len(all_pols)}: {len(all_politys_on_the_polity_list_page)} were taken care of.")
        

        return context

class PolityDetailView(SuccessMessageMixin, generic.DetailView):
    model = Polity
    template_name = "core/polity/polity_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["all_data"] = get_all_data_for_a_polity(self.object.pk, "crisisdb") 
            context["all_general_data"] = get_all_general_data_for_a_polity(self.object.pk)
            context["all_sc_data"] = get_all_sc_data_for_a_polity(self.object.pk)
            context["all_wf_data"] = get_all_wf_data_for_a_polity(self.object.pk)
            context["all_crisis_cases_data"] = get_all_crisis_cases_data_for_a_polity(self.object.pk)
            context["all_power_transitions_data"] = get_all_power_transitions_data_for_a_polity(self.object.pk)
            all_Ras = Polity_research_assistant.objects.filter(polity_id=self.object.pk)
            all_Ras_ids = all_Ras.values_list('polity_ra_id', flat=True)
            experts = Seshat_Expert.objects.filter(id__in=all_Ras_ids)
            
            all_general_ras = []
            for xx in experts:
                an_ra = xx.user.first_name + " " + xx.user.last_name
                if an_ra not in all_general_ras:
                    all_general_ras.append(an_ra)

            all_general_ras_string = ", ".join(all_general_ras)

            

            #my_users_general = [User.objects.get(pk=aa.polity_ra_id) for aa in all_Ras]
            context["majid"] = {"utm_zone": "benam"}
            context["all_Ras"] = all_general_ras_string

        except:
            context["all_data"] = None
            context["all_general_data"] = None
            context["all_sc_data"] = None
            context["all_wf_data"] = None


        #x = polity_detail_data_collector(self.object.pk)
        #context["all_data"] = dict(x)
        #print(self.object.pk)
        context["all_vars"] = {
            "arable_land": "arable_land",
            "agricultural_population": "agricultural_population",
        }
        try:
            my_pol = Polity.objects.get(pk=self.object.pk)
            nga_pol_rels = my_pol.polity_sides.all()
            time_deltas = []
            for nga_pol_rel in nga_pol_rels:
                if (nga_pol_rel.year_from, nga_pol_rel.year_to) not in time_deltas:
                    time_deltas.append((nga_pol_rel.year_from, nga_pol_rel.year_to))

            concise_rels = {}
            for time_delta in time_deltas:
                nga_list = []
                for nga_pol_rel in nga_pol_rels:
                    if time_delta[0] == nga_pol_rel.year_from and time_delta[1] == nga_pol_rel.year_to:
                        nga_list.append(nga_pol_rel.nga_party)
                
                concise_rels[time_delta] = nga_list # "  ~~~   ".join(nga_list)
            context["nga_pol_rel"] = concise_rels
            #print("__________________________")
        except:
            context["nga_pol_rel"] = None
            #print("*************")

        return context


    
# NGA

class NgaCreate(PermissionRequiredMixin, CreateView):
    model = Nga
    form_class = NgaForm
    template_name = "core/nga/nga_form.html"
    permission_required = 'core.add_capital'
    success_url = reverse_lazy('ngas')

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponseRedirect(reverse('seshat-index'))


class NgaUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Nga
    form_class = NgaForm
    template_name = "core/nga/nga_update.html"
    permission_required = 'core.add_capital'
    success_message = "You successfully updated the Nga."
    success_url = reverse_lazy('ngas')


class NgaListView(generic.ListView):
    model = Nga
    template_name = "core/nga/nga_list.html"
    #paginate_by = 10

class NgaDetailView(generic.DetailView):
    model = Nga
    template_name = "core/nga/nga_detail.html"


# Capital

class CapitalCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Capital
    form_class = CapitalForm
    template_name = "core/capital/capital_form_create.html"
    permission_required = 'core.add_capital'
    success_message = "You successfully created a new Capital."
    success_url = reverse_lazy('capitals')

    # def form_valid(self, form):
    #     return super().form_valid(form)
    
    # def form_invalid(self, form):
    #     return HttpResponseRedirect(reverse('capital-create'))


class CapitalUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Capital
    form_class = CapitalForm
    template_name = "core/capital/capital_form.html"
    permission_required = 'core.add_capital'
    success_message = "You successfully updated the Capital."
    success_url = reverse_lazy('capitals')


class CapitalListView(generic.ListView):
    model = Capital
    template_name = "core/capital/capital_list.html"
    #paginate_by = 10

    def get_absolute_url(self):
        return reverse('capitals')
    

class CapitalDelete(PermissionRequiredMixin, DeleteView):
    model = Capital
    success_url = reverse_lazy('capitals')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'
    success_message = "You successfully deleted one Capital."

    

@permission_required('core.view_capital')
def capital_download(request):
    items = Capital.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="capitals.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['capital', 'polity_old_ID', 'polity_new_ID', 'polity_long_name',
                     'current_country', 'longitude', 'latitude','is_verified', 'note'])

    for obj in items:
        writer.writerow([obj.name, obj.polity_cap.name, obj.polity_cap.new_name, obj.polity_cap.long_name, obj.current_country, obj.longitude, obj.latitude, obj.is_verified, obj.note])

    return response


def signup_traditional(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            #current_site = get_current_site(request)
            #subject = 'Activate Your Seshat Account'
            #message = render_to_string('core/account_activation_email.html', {
            #     'user': user,
            #     'domain': current_site,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': account_activation_token.make_token(user)
            # })
            #user.email_user(subject, message)
            # to_be_sent_email = EmailMessage(subject=subject, body=message,
            #                                 from_email=settings.EMAIL_FROM_USER, to=[user.email])

            # #print(settings.EMAIL_HOST_USER)
            # to_be_sent_email.send()
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'core/signup_traditional.html', {'form': form})


def signupfollowup(request):
    print(settings.EMAIL_HOST_USER)
    return render(request, 'core/signup-followup.html')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        #uid = str(urlsafe_base64_decode(uidb64))

        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('signup-followup')
    else:
        return render(request, 'core/account_activation_invalid.html')


# Discussion Room
def discussion_room(request):
    return render(request, 'core/discussion_room.html')

# NLP Room 1
def nlp_datapoints(request):
    return render(request, 'core/nlp_datapoints.html')

# NLP Room 2
def nlp_datapoints_2(request):
    return render(request, 'core/nlp_datapoints_2.html')

def account_activation_sent(request):
    return render(request, 'core/account_activation_sent.html')


def variablehierarchysetting(request):
    my_vars = dic_of_all_vars()
    my_vars_keys = list(my_vars.keys())
    my_vars_good_keys = []
    for item in my_vars_keys:
        good_key = item[0:9] + item[9].lower() + item[10:]
        good_key = good_key.replace('gdp', 'GDP')
        good_key = good_key.replace('gDP', 'GDP')
        my_vars_good_keys.append(good_key)
    all_var_hiers_to_be_hidden = Variablehierarchy.objects.filter(is_verified=True)
    all_var_hiers_to_be_hidden_names = []
    for var in all_var_hiers_to_be_hidden:
        with_crisisdb_name = "crisisdb_" + var.name
        var_name = with_crisisdb_name[0:9] + with_crisisdb_name[9].lower() + with_crisisdb_name[10:]
        var_name = var_name.replace('gdp', 'GDP')
        var_name = var_name.replace('gDP', 'GDP')

        if with_crisisdb_name in my_vars_good_keys:
            var_name = with_crisisdb_name[0:9] + with_crisisdb_name[9].lower() + with_crisisdb_name[10:]
            var_name = var_name.replace('gdp', 'GDP')
            var_name = var_name.replace('gDP', 'GDP')

            all_var_hiers_to_be_hidden_names.append(var_name)
    print('I am here...\n\n')
    #print(all_var_hiers_to_be_hidden_names)
    my_vars_tuple = [('', ' -- Select a CrisisDB Variable -- ')]
    for var in my_vars_good_keys:
        if var not in all_var_hiers_to_be_hidden_names:
            without_crisisdb_var = var[9:]
            var_name = without_crisisdb_var[0].lower() + without_crisisdb_var[1:]
            var_name = var_name.replace('gdp', 'GDP')
            var_name = var_name.replace('gDP', 'GDP')

            my_var_tuple = (var_name, var_name)
            my_vars_tuple.append(my_var_tuple)

    all_sections = Section.objects.all()
    all_sections_tuple = [('', ' -- Select Section -- ')]
    for section in all_sections:
        my_section = section.name
        my_section_tuple = (my_section, my_section)
        all_sections_tuple.append(my_section_tuple)
    # subsections
    all_subsections = Subsection.objects.all()
    all_subsections_tuple = [('', ' -- Select Section First -- ')]
    for subsection in all_subsections:
        my_subsection = subsection.name
        my_subsection_tuple = (my_subsection, my_subsection)
        all_subsections_tuple.append(my_subsection_tuple)
    # Let's create an API serializer for section and subsection heierarchy
    url = "http://127.0.0.1:8000/api/sections/"
    #url = "https://www.majidbenam.com/api/sections/"
    #url = settings.MY_CURRENT_SERVER + "/api/sections/"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    resp = requests.get(url, headers=headers)

    all_my_data = resp.json()['results']
    sections_tree = {}
    sections_options_for_JS = {}
    for list_item in all_my_data:
        subsect_dic = {}
        subsects_only_list = []
        for subsec in list_item['subsections']:
            list_to_be = []
            subsects_only_list.append(subsec)
            sel_sect = Section.objects.get(name=list_item['name'])
            sel_subsect = Subsection.objects.get(name=subsec)
            my_selected_vars_objects = Variablehierarchy.objects.filter( section=sel_sect, subsection=sel_subsect,)
            for var_obj in my_selected_vars_objects:
                #print(var_obj)
                list_to_be.append(var_obj.name)
            subsect_dic[subsec] = list_to_be
        sections_tree[list_item['name']] = subsect_dic
        sections_options_for_JS[list_item['name']] = subsects_only_list
    context = {
        'sectionOptions': sections_options_for_JS, 
        'section_tree_data': sections_tree,
    }
    #print(context['sectionOptions'])
    #print(context['section_tree_data'])


    if request.method == 'POST':
        form = VariablehierarchyFormNew(request.POST)
        if True:
            data = request.POST
            variable_name = data["variable_name"]
            #is_verified_str = data["is_verified"]
            is_verified_str = data.get("is_verified", False)
            if is_verified_str == 'on':
                is_verified = True
            elif is_verified_str == 'off':
                is_verified = False
            else:
                is_verified = False
            section_name = Section.objects.get(name=data["section_name"])
            subsection_name = Subsection.objects.get(
                name=data["subsection_name"])
            # check to see if subsection and section match
            if data["subsection_name"] in sections_tree[data["section_name"]]:
                new_var_hierarchy = Variablehierarchy(
                    name=variable_name, section=section_name, subsection=subsection_name,  is_verified=is_verified)
                new_var_hierarchy.save()
                #print('Valid Foooooooooooorm: \n\n',)
                # print(data)
                my_message = f'''You have successfully submitted {variable_name} to: {section_name} >  {subsection_name}'''
                messages.success(request, my_message)
                return HttpResponseRedirect(reverse('variablehierarchysetting'))
            else:
                messages.warning(request, 'Form submission unssuccessful, section and subsection do not match.')
                #return render(request, 'core/Variablehierarchy.html', {'form': VariablehierarchyFormNew()})

        else:
            data = request.POST
            #print('halllooooooooo:', data["variable_name"])
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)

    else:
        form = VariablehierarchyFormNew()
    context['form'] = form
    context['variable_list'] = list(my_vars_tuple)
    context['section_list'] = list(all_sections_tuple)
    context['subsection_list'] = list(all_subsections_tuple)

    #context['SuccessMessage'] = "Done Perfectly."
    return render(request, 'core/variablehierarchy.html', context)



###############
def do_zotero(results):
    import re
    mother_ref_dic = []
    for i, item in enumerate(results):
        #print(i, ": ", item['data']['key'], item['data']['date'])
        #if item['data']['key'] in ["MJT9UJE4", "NIKCMK5L", "QTI79LX9"]:
        #    print("______________")
        #    print(item)
        a_key = item['data']['key']
        if a_key == "3BQQ8WN8":
            print("I skipped over  youuuuu: 3BQQ8WN8 because you are not in the database!")
            continue
        if a_key == 'RR6R3383':
            print("I skipped over  youuuuu: RR6R3383 because your title is too big")
            continue
            
            #print(pprint.pprint(item))
        try:
            # we need to make sure that all the changes in Zotero will be reflected here.
            potential_new_ref = Reference.objects.get(zotero_link=a_key)
            # full_date = item['data'].get('date')
            # if full_date:
            #     year = re.search(r'[12]\d{3}', full_date)
            #     if year:
            #         year_int = int(year[0])
            #         if potential_new_ref.year != year_int:
            #             print(f"Item Changed On Zotero: {a_key}")
            continue
        except:          
            my_dic = {}
            try:
                if item['data']['key']:
                    tuple_key = item['data']['key']
                    my_dic['key'] = tuple_key
                else:
                    pass #print("key is empty for index: ", i, item['data']['itemType'])
            except:
                pass #print("No key for item with index: ", i)
            try:
                if item['data']['itemType']:
                    tuple_item = item['data']['itemType']
                    my_dic['itemType'] = tuple_item
                else:
                    pass #print("itemType is empty for index: ", i, item['data']['itemType'])
            except:
                pass #print("No itemType for item with index: ", i)
            try:
                num_of_creators = len(item['data']['creators'])
                if num_of_creators < 4 and num_of_creators > 0:
                    all_creators_list = []  
                    for j in range(num_of_creators):
                        if a_key == "MM6AEU7H":
                            print("I saw youuuuuuuuuuuuuuu more probably because you have contributors instead of authors")
                        try:
                            try:
                                good_name = item['data']['creators'][j]['lastName']
                            except:
                                good_name = item['data']['creators'][j]['name']
                        except:
                            good_name = ("NO_NAMES",)
                        all_creators_list.append(good_name)
                    good_name_with_space = "_".join(all_creators_list)
                    good_name_with_underscore = good_name_with_space.replace(' ', '_')
                    my_dic['mainCreator'] = good_name_with_underscore
                elif num_of_creators > 3:
                    try:
                        try:
                            good_name = item['data']['creators'][0]['lastName']
                        except:
                            good_name = item['data']['creators'][0]['name']
                    except:
                        good_name = ("NO_NAME",)
                    good_name_with_space = good_name + '_et_al'
                    good_name_with_underscore = good_name_with_space.replace(' ', '_')
                    my_dic['mainCreator'] = good_name_with_underscore
                else:
                    my_dic['mainCreator'] = "NO_CREATOR" 
                #pass #print(my_dic['mainCreator'])
            except:
                my_dic['mainCreator'] = "NO_CREATORS"
                pass #print("No mainCreator for item with index: ", i, item['data']['itemType'])
            try:
                if item['data']['date']:
                    full_date = item['data']['date']
                    year = re.search(r'[12]\d{3}', full_date)
                    year_int = int(year[0])
                    my_dic['year'] = year_int
                else:
                    my_dic['year'] = 0
                    #pass #print("year is empty for index: ", i, item['data']['itemType'])
                #pass #print(my_dic['year'])
            except:
                my_dic['year'] = -1
                #pass #print("No year for item with index: ", i, item['data']['itemType'])
            try:
                try:
                    if item['data']['bookTitle']:
                        if a_key == "MM6AEU7H":
                            print("I saw youuuuuuuuuuuuuuu more")
                        if item['data']['itemType'] == 'bookSection':
                            good_title = item['data']['title'] + " (IN) " + item['data']['bookTitle']
                            pass #print (i, ": ", a_key, "    ", good_title)
                        else:
                            good_title = item['data']['title']
                            pass #print (i, ": ", a_key, "    ", good_title)
                        counter_bookTitle = counter_bookTitle + 1
                        my_dic['title'] = good_title
                    else:
                        good_title = item['data']['title']
                        my_dic['title'] = good_title
                        if a_key == "MM6AEU7H":
                            print("I saw youuuuuuuuuuuuuuu more")
                        pass #print (i, ": ", a_key, "    ", good_title)
                except:
                    my_dic['title'] = item['data']['title']
                    pass #print (i, ": ", a_key, "    ", item['data']['title'])
            except:
                pass #print("No title for item with index: ", i)
            
            pot_title = my_dic.get('title')
            if not pot_title:
                pot_title = "NO_TITLE_PROVIDED_IN_ZOTERO"
            #print("Years: ", my_dic.get('year'))
            #print("****************")
            newref = Reference(title=pot_title, year=my_dic.get('year'), creator=my_dic.get('mainCreator'), zotero_link=my_dic.get('key'))
            #newref = Reference(title=my_dic['title'], year=my_dic['year'], creator=my_dic['mainCreator'], zotero_link=my_dic['key'])

            if my_dic.get('year') < 2040:
                newref.save()
                mother_ref_dic.append(my_dic)

    #print(len(mother_ref_dic))
    #print(counter_bookTitle)
    print("Bye Zotero")
    return mother_ref_dic

def do_zotero_manually(results):
    mother_ref_dic = []
    for i, item in enumerate(results):

        a_key = item['key']
        if a_key == "3BQQ8WN8":
            print("I skipped over  youuuuu: 3BQQ8WN8 because you are not in the database!")
            continue
        if a_key == 'RR6R3383':
            print("I skipped over  youuuuu: RR6R3383 because your title is too big")
            continue
            
        try:
            potential_new_ref = Reference.objects.get(zotero_link=a_key)
            continue
        except:          
            my_dic = {}
            my_dic['key'] = a_key
            my_dic['mainCreator'] = item['mainCreator']
            my_dic['year'] = item['year']
            my_dic['title'] = item['title']

            newref = Reference(title=my_dic.get('title'), year=my_dic.get('year'), creator=my_dic.get('mainCreator'), zotero_link=my_dic.get('key'))

            if my_dic.get('year') < 2040:
                newref.save()
                mother_ref_dic.append(my_dic)


    print("Bye Zotero Manually")
    return mother_ref_dic


##########

def update_citations_from_inside_zotero_update():
    """
    this function gets all the references and build a citation for them
    """
    from datetime import datetime
    all_refs = Reference.objects.all()
    for ref in all_refs:
        a_citation = Citation.objects.get_or_create(ref=ref, page_from=None, page_to=None)
        a_citation[0].save()
    print("Halllooooo")
    # Citation.objects.bulk_create(all_citations)
    #return render (request, 'core/references/reference_list.html')

###########


def synczoteromanually(request):
    print("Hallo Zotero Manually")
    from .manual_input_refs import manual_input_refs 

    new_refs = do_zotero_manually(manual_input_refs)
    context = {}
    context["newly_adds"] = new_refs
    update_citations_from_inside_zotero_update()
    return render (request, 'core/references/synczotero.html', context)

def synczotero(request):
    print("Hallo Zotero")

    from pyzotero import zotero
    zot = zotero.Zotero(1051264, 'group', 'VF5X3TCC3bUYov8Au5gCHf3a')
    results = zot.everything(zot.top())
    #results = zot.top(limit=100)

    print(len(results))
    counter_bookTitle = 0
    new_refs = do_zotero(results[0:300])
    context = {}
    context["newly_adds"] = new_refs
    update_citations_from_inside_zotero_update()
    #num_1_ref = Reference.objects.get(zotero_link ="FGFSZUNB")
    #num_1_ref.year = 2014
    #num_1_ref.save()
    return render (request, 'core/references/synczotero.html', context)

def synczotero100(request):
    print("Hallo Zotero")

    from pyzotero import zotero
    zot = zotero.Zotero(1051264, 'group', 'VF5X3TCC3bUYov8Au5gCHf3a')
    #results = zot.everything(zot.top())
    results = zot.top(limit=100)

    print(len(results))
    counter_bookTitle = 0
    new_refs = do_zotero(results)
    context = {}
    context["newly_adds"] = new_refs
    update_citations_from_inside_zotero_update()
    #num_1_ref = Reference.objects.get(zotero_link ="FGFSZUNB")
    #num_1_ref.year = 2014
    #num_1_ref.save()
    return render (request, 'core/references/synczotero.html', context)



def update_citations(request):
    """
    this function gets all the references and build a citation for them
    """
    all_refs = Reference.objects.all()
    for ref in all_refs:
        a_citation = Citation.objects.get_or_create(ref=ref, page_from=None, page_to=None)
        a_citation[0].save()
    # Citation.objects.bulk_create(all_citations)
    return render (request, 'core/references/reference_list.html')


@require_GET
def polity_filter_options_view(request):
    search_text = request.GET.get('search_text', '')

    # Filter the options based on the search text
    options = Polity.objects.filter(name__icontains=search_text).values('id', 'name')

    response = {
        'options': list(options)
    }
    return JsonResponse(response)


def download_oldcsv(request, file_name):
    file_path = os.path.join(settings.STATIC_ROOT, 'csvfiles', file_name)
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response

# Shapefile views

def map_view(request, data='macrostate'):
    """
        This view is used to display a map with polities plotted on it.
    """
    
    # Determine which shape data to plot
    if data == 'macrostate':
        shapes = MacrostateShapefile.objects.all()

        all_years = set()

        for shape in shapes:
            if shape.date_from is not None and shape.date_to is not None:
                start_year = int(shape.date_from[:-3] if 'BCE' in shape.date_from else shape.date_from[:-2])
                end_year = int(shape.date_to[:-3] if 'BCE' in shape.date_to else shape.date_to[:-2])

                # For BCE dates, make the value negative
                if 'BCE' in shape.date_from:
                    start_year = -start_year
                if 'BCE' in shape.date_to:
                    end_year = -end_year

                all_years.add(start_year)
                all_years.add(end_year)

                shape.start_year = start_year
                shape.end_year = end_year

        # Filter out the unique years and sort them
        unique_years = sorted(all_years)

        # Get a list of centuries
        earliest_century = floor(unique_years[0] / 100) * 100
        latest_century = ceil(unique_years[-1] / 100) * 100
        centuries = [num for num in range(earliest_century, latest_century + 1) if num % 100 == 0]
        century_strings = []
        for century in centuries:
            if century < 0:
                century_strings.append(str(abs(century)) + "BCE")
            else:
                century_strings.append(str(century) + "CE")
        centuries_zipped = zip(centuries, century_strings)
        content = {'shapes': shapes,
                   'unique_years': unique_years,
                   'centuries': dict(centuries_zipped),
                   'data': data
                   }

    elif data == 'gadm':
        shapes = GADMShapefile.objects.all()
        content = {'shapes': shapes,
                   'data': data
                   }
    
    return render(request,
                  'core/spatial_map.html',
                  content
                  )

def gadm_map_view(request):
    query = """
        SELECT 
            "COUNTRY",
            ST_Union(geom) AS aggregated_geometry
        FROM 
            core_gadmshapefile
        WHERE 
            "COUNTRY" = 'Austria'
        GROUP BY 
            "COUNTRY";
    """

    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

    # Process the result
    shapes = [{'country': row[0], 'aggregated_geometry': GEOSGeometry(row[1]).geojson} for row in rows]

    content = {'shapes': shapes}
    
    return render(request,
                  'core/gadm_map.html',
                  content
                  )