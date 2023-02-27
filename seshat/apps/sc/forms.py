from .models import Ra, Polity_territory, Polity_population, Population_of_the_largest_settlement, Settlement_hierarchy, Administrative_level, Religious_level, Military_level, Professional_military_officer, Professional_soldier, Professional_priesthood, Full_time_bureaucrat, Examination_system, Merit_promotion, Specialized_government_building, Formal_legal_code, Judge, Court, Professional_lawyer, Irrigation_system, Drinking_water_supply_system, Market, Food_storage_site, Road, Bridge, Canal, Port, Mines_or_quarry, Mnemonic_device, Nonwritten_record, Written_record, Script, Non_phonetic_writing, Phonetic_alphabetic_writing, Lists_tables_and_classification, Calendar, Sacred_text, Religious_literature, Practical_literature, History, Philosophy, Scientific_literature, Fiction, Article, Token, Precious_metal, Foreign_coin, Indigenous_coin, Paper_currency, Courier, Postal_station, General_postal_service
import datetime

from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.widgets import Textarea

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.widgets import FilteredSelectMultiple

from django.template.defaulttags import register

commonlabels = {
    'year_from': 'Start Year',
    'year_to': 'End Year',
    'tag': 'Confidence Level',
    "is_disputed" : "&nbsp; <b> There is a Dispute? </b>",
    "expert_reviewed" : "&nbsp; Expert Checked?",
    "drb_reviewed" : "&nbsp; Data Review Board Reviewed?",
    'citations': 'Add one or more Citations',
    'finalized': 'This piece of data is verified.',
}

commonfields = ['polity', 'year_from', 'year_to',
                'description', 'tag', 'is_disputed', 'expert_reviewed', 'drb_reviewed', 'finalized', 'citations']

commonwidgets = {
    'polity': forms.Select(attrs={'class': 'form-control  mb-3', }),
    'year_from': forms.NumberInput(attrs={'class': 'form-control  mb-3',}),
    'year_to': forms.NumberInput(attrs={'class': 'form-control  mb-3', }),
    'description': Textarea(attrs={'class': 'form-control  mb-3', 'style': 'height: 140px', 'placeholder':'Add a meaningful description (optional)'}),
    'citations': forms.SelectMultiple(attrs={'class': 'form-control mb-3 js-states js-example-basic-multiple', 'text':'citations[]' , 'style': 'height: 340px', 'multiple': 'multiple'}),
    'tag': forms.RadioSelect(),
    "is_disputed" : forms.CheckboxInput(attrs={'class': 'mb-3', }),
    "expert_reviewed" : forms.CheckboxInput(attrs={'class': 'mb-3', }),
    "drb_reviewed" : forms.CheckboxInput(attrs={'class': 'mb-3', }),
    'finalized': forms.CheckboxInput(attrs={'class': 'mb-3', 'checked': True, }),
}

class RaForm(forms.ModelForm):
    class Meta:
        model = Ra
        fields = commonfields.copy()
        fields.append('sc_ra')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['sc_ra'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Polity_territoryForm(forms.ModelForm):
    class Meta:
        model = Polity_territory
        fields = commonfields.copy()
        fields.append('polity_territory_from')
        fields.append('polity_territory_to')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['polity_territory_from'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['polity_territory_to'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Polity_populationForm(forms.ModelForm):
    class Meta:
        model = Polity_population
        fields = commonfields.copy()
        fields.append('polity_population_from')
        fields.append('polity_population_to')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['polity_population_from'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['polity_population_to'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Population_of_the_largest_settlementForm(forms.ModelForm):
    class Meta:
        model = Population_of_the_largest_settlement
        fields = commonfields.copy()
        fields.append('population_of_the_largest_settlement_from')
        fields.append('population_of_the_largest_settlement_to')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['population_of_the_largest_settlement_from'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['population_of_the_largest_settlement_to'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Settlement_hierarchyForm(forms.ModelForm):
    class Meta:
        model = Settlement_hierarchy
        fields = commonfields.copy()
        fields.append('settlement_hierarchy_from')
        fields.append('settlement_hierarchy_to')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['settlement_hierarchy_from'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['settlement_hierarchy_to'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Administrative_levelForm(forms.ModelForm):
    class Meta:
        model = Administrative_level
        fields = commonfields.copy()
        fields.append('administrative_level_from')
        fields.append('administrative_level_to')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['administrative_level_from'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['administrative_level_to'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Religious_levelForm(forms.ModelForm):
    class Meta:
        model = Religious_level
        fields = commonfields.copy()
        fields.append('religious_level_from')
        fields.append('religious_level_to')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['religious_level_from'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['religious_level_to'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Military_levelForm(forms.ModelForm):
    class Meta:
        model = Military_level
        fields = commonfields.copy()
        fields.append('military_level_from')
        fields.append('military_level_to')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['military_level_from'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['military_level_to'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Professional_military_officerForm(forms.ModelForm):
    class Meta:
        model = Professional_military_officer
        fields = commonfields.copy()
        fields.append('professional_military_officer')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['professional_military_officer'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Professional_soldierForm(forms.ModelForm):
    class Meta:
        model = Professional_soldier
        fields = commonfields.copy()
        fields.append('professional_soldier')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['professional_soldier'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Professional_priesthoodForm(forms.ModelForm):
    class Meta:
        model = Professional_priesthood
        fields = commonfields.copy()
        fields.append('professional_priesthood')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['professional_priesthood'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Full_time_bureaucratForm(forms.ModelForm):
    class Meta:
        model = Full_time_bureaucrat
        fields = commonfields.copy()
        fields.append('full_time_bureaucrat')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['full_time_bureaucrat'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Examination_systemForm(forms.ModelForm):
    class Meta:
        model = Examination_system
        fields = commonfields.copy()
        fields.append('examination_system')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['examination_system'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Merit_promotionForm(forms.ModelForm):
    class Meta:
        model = Merit_promotion
        fields = commonfields.copy()
        fields.append('merit_promotion')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['merit_promotion'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Specialized_government_buildingForm(forms.ModelForm):
    class Meta:
        model = Specialized_government_building
        fields = commonfields.copy()
        fields.append('specialized_government_building')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['specialized_government_building'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Formal_legal_codeForm(forms.ModelForm):
    class Meta:
        model = Formal_legal_code
        fields = commonfields.copy()
        fields.append('formal_legal_code')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['formal_legal_code'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class JudgeForm(forms.ModelForm):
    class Meta:
        model = Judge
        fields = commonfields.copy()
        fields.append('judge')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['judge'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class CourtForm(forms.ModelForm):
    class Meta:
        model = Court
        fields = commonfields.copy()
        fields.append('court')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['court'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Professional_lawyerForm(forms.ModelForm):
    class Meta:
        model = Professional_lawyer
        fields = commonfields.copy()
        fields.append('professional_lawyer')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['professional_lawyer'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Irrigation_systemForm(forms.ModelForm):
    class Meta:
        model = Irrigation_system
        fields = commonfields.copy()
        fields.append('irrigation_system')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['irrigation_system'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Drinking_water_supply_systemForm(forms.ModelForm):
    class Meta:
        model = Drinking_water_supply_system
        fields = commonfields.copy()
        fields.append('drinking_water_supply_system')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['drinking_water_supply_system'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class MarketForm(forms.ModelForm):
    class Meta:
        model = Market
        fields = commonfields.copy()
        fields.append('market')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['market'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Food_storage_siteForm(forms.ModelForm):
    class Meta:
        model = Food_storage_site
        fields = commonfields.copy()
        fields.append('food_storage_site')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['food_storage_site'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class RoadForm(forms.ModelForm):
    class Meta:
        model = Road
        fields = commonfields.copy()
        fields.append('road')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['road'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class BridgeForm(forms.ModelForm):
    class Meta:
        model = Bridge
        fields = commonfields.copy()
        fields.append('bridge')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['bridge'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class CanalForm(forms.ModelForm):
    class Meta:
        model = Canal
        fields = commonfields.copy()
        fields.append('canal')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['canal'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class PortForm(forms.ModelForm):
    class Meta:
        model = Port
        fields = commonfields.copy()
        fields.append('port')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['port'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Mines_or_quarryForm(forms.ModelForm):
    class Meta:
        model = Mines_or_quarry
        fields = commonfields.copy()
        fields.append('mines_or_quarry')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['mines_or_quarry'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Mnemonic_deviceForm(forms.ModelForm):
    class Meta:
        model = Mnemonic_device
        fields = commonfields.copy()
        fields.append('mnemonic_device')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['mnemonic_device'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Nonwritten_recordForm(forms.ModelForm):
    class Meta:
        model = Nonwritten_record
        fields = commonfields.copy()
        fields.append('nonwritten_record')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['nonwritten_record'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Written_recordForm(forms.ModelForm):
    class Meta:
        model = Written_record
        fields = commonfields.copy()
        fields.append('written_record')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['written_record'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class ScriptForm(forms.ModelForm):
    class Meta:
        model = Script
        fields = commonfields.copy()
        fields.append('script')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['script'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Non_phonetic_writingForm(forms.ModelForm):
    class Meta:
        model = Non_phonetic_writing
        fields = commonfields.copy()
        fields.append('non_phonetic_writing')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['non_phonetic_writing'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Phonetic_alphabetic_writingForm(forms.ModelForm):
    class Meta:
        model = Phonetic_alphabetic_writing
        fields = commonfields.copy()
        fields.append('phonetic_alphabetic_writing')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['phonetic_alphabetic_writing'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Lists_tables_and_classificationForm(forms.ModelForm):
    class Meta:
        model = Lists_tables_and_classification
        fields = commonfields.copy()
        fields.append('lists_tables_and_classification')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['lists_tables_and_classification'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = commonfields.copy()
        fields.append('calendar')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['calendar'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Sacred_textForm(forms.ModelForm):
    class Meta:
        model = Sacred_text
        fields = commonfields.copy()
        fields.append('sacred_text')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['sacred_text'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Religious_literatureForm(forms.ModelForm):
    class Meta:
        model = Religious_literature
        fields = commonfields.copy()
        fields.append('religious_literature')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['religious_literature'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Practical_literatureForm(forms.ModelForm):
    class Meta:
        model = Practical_literature
        fields = commonfields.copy()
        fields.append('practical_literature')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['practical_literature'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = commonfields.copy()
        fields.append('history')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['history'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class PhilosophyForm(forms.ModelForm):
    class Meta:
        model = Philosophy
        fields = commonfields.copy()
        fields.append('philosophy')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['philosophy'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Scientific_literatureForm(forms.ModelForm):
    class Meta:
        model = Scientific_literature
        fields = commonfields.copy()
        fields.append('scientific_literature')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['scientific_literature'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class FictionForm(forms.ModelForm):
    class Meta:
        model = Fiction
        fields = commonfields.copy()
        fields.append('fiction')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['fiction'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = commonfields.copy()
        fields.append('article')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['article'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class TokenForm(forms.ModelForm):
    class Meta:
        model = Token
        fields = commonfields.copy()
        fields.append('token')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['token'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Precious_metalForm(forms.ModelForm):
    class Meta:
        model = Precious_metal
        fields = commonfields.copy()
        fields.append('precious_metal')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['precious_metal'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Foreign_coinForm(forms.ModelForm):
    class Meta:
        model = Foreign_coin
        fields = commonfields.copy()
        fields.append('foreign_coin')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['foreign_coin'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Indigenous_coinForm(forms.ModelForm):
    class Meta:
        model = Indigenous_coin
        fields = commonfields.copy()
        fields.append('indigenous_coin')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['indigenous_coin'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Paper_currencyForm(forms.ModelForm):
    class Meta:
        model = Paper_currency
        fields = commonfields.copy()
        fields.append('paper_currency')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['paper_currency'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class CourierForm(forms.ModelForm):
    class Meta:
        model = Courier
        fields = commonfields.copy()
        fields.append('courier')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['courier'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Postal_stationForm(forms.ModelForm):
    class Meta:
        model = Postal_station
        fields = commonfields.copy()
        fields.append('postal_station')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['postal_station'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class General_postal_serviceForm(forms.ModelForm):
    class Meta:
        model = General_postal_service
        fields = commonfields.copy()
        fields.append('general_postal_service')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['general_postal_service'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        