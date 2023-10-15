
########## Beginning of Model Imports
from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
#from model_utils.models import StatusModel
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.core.validators import MinValueValidator

from datetime import date

import uuid

from django.utils import translation

from ..core.models import SeshatCommon, Certainty, Tags, Section, Subsection, Polity
from seshat.apps.accounts.models import Seshat_Expert

########## End of Model Imports

########## Beginning of tuple choices for CrisisDB Models
HUMAN_SACRIFICE_HUMAN_SACRIFICE_CHOICES = (
('U', 'Unknown'),
('P', 'Present'),
('A~P', 'Transitional (Absent -> Present)'),
('A', 'Absent'),
('P~A', 'Transitional (Present -> Absent)'),
)

CRISIS_CONSEQUENCE_CHOICES = (
('U', 'Unknown'),
('SU', 'Suspected Unknown'),
('P', 'Present'),
('A', 'Absent'),
('IP', 'Inferred Present'),
('IA', 'Inferred Absent'),
('DIS', 'Disputed'),
)

SUB_CATEGORY_DISEASE_OUTBREAK_CHOICES = (
('Peculiar Epidemics', 'Peculiar Epidemics'),
('Pestilence', 'Pestilence'),
('Miasm', 'Miasm'),
('Pox', 'Pox'),
('Uncertain Pestilence', 'Uncertain Pestilence'),
('Dysentery', 'Dysentery'),
('Malaria', 'Malaria'),
('Influenza', 'Influenza'),
('Cholera', 'Cholera'),
('Diptheria', 'Diptheria'),
('Plague', 'Plague'),
)

MAGNITUDE_DISEASE_OUTBREAK_CHOICES = (
('Uncertain', 'Uncertain'),
('Light', 'Light'),
('Heavy', 'Heavy'),
('No description', 'No description'),
('Heavy- Multiple Times', 'Heavy- Multiple Times'),
('No Happening', 'No Happening'),
('Moderate', 'Moderate'),
)

DURATION_DISEASE_OUTBREAK_CHOICES = (
('No description', 'No description'),
('Over 90 Days', 'Over 90 Days'),
('Uncertain', 'Uncertain'),
('30-60 Days', '30-60 Days'),
('1-10 Days', '1-10 Days'),
('60-90 Days', '60-90 Days'),
)

US_STATE_CHOICES = (
("AL", "Alabama"),
("AK", "Alaska"),
("AZ", "Arizona"),
("AR", "Arkansas"),
("CA", "California"),
("CO", "Colorado"),
("CT", "Connecticut"),
("DE", "Delaware"),
("FL", "Florida"),
("GA", "Georgia"),
("HI", "Hawaii"),
("ID", "Idaho"),
("IL", "Illinois"),
("IN", "Indiana"),
("IA", "Iowa"),
("KS", "Kansas"),
("KY", "Kentucky"),
("LA", "Louisiana"),
("ME", "Maine"),
("MD", "Maryland"),
("MA", "Massachusetts"),
("MI", "Michigan"),
("MN", "Minnesota"),
("MS", "Mississippi"),
("MO", "Missouri"),
("MT", "Montana"),
("NE", "Nebraska"),
("NV", "Nevada"),
("NH", "New Hampshire"),
("NJ", "New Jersey"),
("NM", "New Mexico"),
("NY", "New York"),
("NC", "North Carolina"),
("ND", "North Dakota"),
("OH", "Ohio"),
("OK", "Oklahoma"),
("OR", "Oregon"),
("PA", "Pennsylvania"),
("RI", "Rhode Island"),
("SC", "South Carolina"),
("SD", "South Dakota"),
("TN", "Tennessee"),
("TX", "Texas"),
("UT", "Utah"),
("VT", "Vermont"),
("VA", "Virginia"),
("WA", "Washington"),
("WV", "West Virginia"),
("WI", "Wisconsin"),
("WY", "Wyoming"),
("UNK", "UNKNOWN"),
)

ATTENTION_TAGS_CHOICES = (
    ('NeedsExpertInput', 'Needs Expert Input'),
    ('IsInconsistent', 'Is Inconsistent'),
    ('IsWrong', 'Is Wrong'),
    ('IsOk', 'IS OK'),
)

VIOLENCE_TYPE_CHOICES = (
('lynching', 'lynching'),
  ('riot', 'riot'), 
  ('executions', 'executions'), 
  ('war', 'war'), 
  ('assassination', 'assassination'), 
  ('compilation', 'compilation'), 
  ('terrorism', 'terrorism'), 
  ('rampage', 'rampage'), 
  ('insurrection', 'insurrection'), 
  ('mass suicide', 'mass suicide'), 
  ('UNKNOWN_INPUT', 'UNKNOWN_INPUT'), 
  ('unknown', 'unknown'), 
  ('revenge', 'revenge')
)




########## END of  tuple choices for CrisisDB Models

def return_beautiful_abs_pres(item):
    if item == "P":
        return '<i class="fa-solid fa-check text-success"></i>'
    elif item == "A":
        return '<i class="fa-sharp fa-solid fa-xmark text-danger"></i>'
    else:
        return "-"


########## Beginning of Function Definitions for CrisisDB Models

def call_my_name(self):
    if self.year_from == self.year_to or ((not self.year_to) and self.year_from):
        return self.name + " [for " + self.polity.name + " in " + str(self.year_from) + "]"
    else:
        return self.name + " [for " + self.polity.name + " from " + str(self.year_from) + " to " + str(self.year_to) + "]"


def return_citations(self):
    return '<br>'.join(['<a href="' + citation.zoteroer() + '">' + '<i class="fa-solid fa-book"></i> ' + citation.full_citation_display() + ' </a>' for citation in self.citations.all()])


def clean_times(self):
    if (self.year_from and self.year_to) and self.year_from > self.year_to:
        raise ValidationError({
            'year_from':  mark_safe('<span class="text-danger"> <i class="fa-solid fa-triangle-exclamation"></i> The start year is bigger than the end year!</span>'),
        })
    if self.year_from and (self.year_from > date.today().year):
        raise ValidationError({
            'year_from':  mark_safe('<span class="text-danger"> <i class="fa-solid fa-triangle-exclamation"></i> The start year is out of range!</span>'),
        })
    if self.year_from and (self.year_from < self.polity.start_year):
        raise ValidationError({
            'year_from': mark_safe('<span class="text-danger"> <i class="fa-solid fa-triangle-exclamation"></i> The start year is earlier than the start year of the corresponding polity!</span>'),
        })
    if self.year_to and (self.year_to > self.polity.end_year):
        raise ValidationError({
            'year_to':  mark_safe('<span class="text-danger"> <i class="fa-solid fa-triangle-exclamation"></i>The end year is later than the end year of the corresponding polity!</span>'),
        })
    if self.year_to and (self.year_to > date.today().year):
        raise ValidationError({
            'year_to': mark_safe('<span class="text-danger"> <i class="fa-solid fa-triangle-exclamation"></i>The end year is out of range!</span>'),
        })

########## End of Function Definitions for CrisisDB Models

################American Violence Models:
class Us_location(models.Model):
    city = models.CharField(max_length=300, null=True, blank=True)
    county = models.CharField(max_length=300, null=True, blank=True)
    special_place = models.CharField(max_length=300, null=True, blank=True)
    us_state = models.CharField(max_length=5, choices=US_STATE_CHOICES, null=True, blank=True)
    attention_tag =  models.CharField(max_length=30, choices=ATTENTION_TAGS_CHOICES, null=True, blank=True)

    class Meta:
        ordering = ['us_state', '-city', '-county', '-special_place']

    # def show_state(self):
    #     if self.us_state and self.us_state != "UNK":
    #         return f'{self.get_us_state_display()} ({self.us_state})'
    #     elif self.us_state and self.us_state == "UNK":
    #         components = []

    #         if self.city and self.county:
    #             components.extend([self.city, self.county])
    #         elif self.city:
    #             components.append(self.city)
    #         elif self.county:
    #             components.append(self.county)
    #         elif self.special_place:
    #             components.append(self.special_place)
    #         return ", ".join(components)
    #     else:
    #         return "Unknown Location"

    def __str__(self):
        components = []

        if self.us_state:
            components.append(f'<b>{self.get_us_state_display()} ({self.us_state})</b>')

        if self.city and self.county:
            components.extend([self.city, self.county])
        elif self.city:
            components.append(self.city)
        elif self.county:
            components.append(self.county)
        elif self.special_place:
            components.append(self.special_place)

        return mark_safe(", ".join(components)) or "Location (No Data)"
    

    
class Us_violence_subtype(models.Model):
    name = models.CharField(max_length=80, null=True, blank=True)
    is_uncertain = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']
    
    def __str__(self) -> str:
        return f"{self.name}{' (?)' if self.is_uncertain else ''}"
    
class Us_violence_data_source(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    abbreviation = models.CharField(max_length=20, null=True, blank=True)
    url_address = models.URLField(max_length=500, null=True, blank=True)
    is_uncertain = models.BooleanField(default=False)
    attention_tag =  models.CharField(max_length=30, choices=ATTENTION_TAGS_CHOICES, null=True, blank=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self) -> str:
        if self.abbreviation:
            return mark_safe(f"<b>{self.abbreviation}</b>: {self.name}{' (?)' if self.is_uncertain else ''}")
        else:
            return f"{self.name}{' (?)' if self.is_uncertain else ''}"
    
    
class Us_violence(models.Model):
    violence_date = models.DateField(null=True, blank=True)
    violence_type = models.CharField(max_length=50, choices=VIOLENCE_TYPE_CHOICES, null=True, blank=True)
    violence_subtype = models.ManyToManyField(Us_violence_subtype, related_name="%(app_label)s_%(class)s_related",related_query_name="%(app_label)s_%(class)ss", blank=True,)
    fatalities = models.IntegerField(validators=[MinValueValidator(0)],blank=True,null=True)
    location = models.ManyToManyField(Us_location, related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)ss", blank=True,)
    url_address = models.URLField(max_length=500, null=True, blank=True)
    short_data_source = models.ManyToManyField(Us_violence_data_source, related_name="%(app_label)s_%(class)s_related", related_query_name="%(app_label)s_%(class)ss", blank=True,)
    source_details = models.TextField(blank=True, null=True,)
    narrative = models.TextField(blank=True, null=True,)

    class Meta:
        ordering = ['-violence_date', "-fatalities"]

    def show_locations(self):
        list_of_locations = list(self.location.all())
        location_str = " / ".join(str(location) for location in list_of_locations)
        return location_str
    

    def show_narrative_without_quotes(self):
        if self.narrative:
            return self.narrative.replace('"', "'")
        else:
            return "No_Narrative"
    
    # def show_states(self):
    #     list_of_locations = list(self.location.all())
    #     location_str = " / ".join(str(location.show_state()) for location in list_of_locations)
    #     return location_str
    
    def show_violence_subtypes(self):
        list_of_subtypes = list(self.violence_subtype.all())
        subtype_str = ", ".join(str(subtype) for subtype in list_of_subtypes)
        return subtype_str
    
    def show_short_data_sources(self):
        list_of_short_data_sources = list(self.short_data_source.all())
        short_data_source_str = ", ".join(str(short_data_source) for short_data_source in list_of_short_data_sources)
        return short_data_source_str
    
    def __str__(self) -> str:
        list_of_locations = list(self.location.all())
        location_str = ": " + " and ".join(str(location) for location in list_of_locations)
        return f"Violence: {self.fatalities} deaths in{location_str}."



###########################

# Beginning of Crisis Consequences Model
class Crisis_consequence(SeshatCommon):
    crisis_case_id = models.CharField(max_length=100)
    other_polity = models.ForeignKey(Polity, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related_other",
                               related_query_name="%(app_label)s_%(class)s_other", null=True, blank=True)
    is_first_100 = models.BooleanField(default=False, blank=True, null=True)
    name = models.CharField(max_length=300, null=True, blank=True)
    decline = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES, null=True, blank=True)
    collapse = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES, null=True, blank=True)
    epidemic = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES, null=True, blank=True)
    downward_mobility = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES, null=True, blank=True)
    extermination = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES, null=True, blank=True)
    uprising = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES, null=True, blank=True)
    revolution = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES, null=True, blank=True)
    successful_revolution = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES, null=True, blank=True)
    civil_war = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES, null=True, blank=True)
    century_plus = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES, null=True, blank=True)
    fragmentation = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES, null=True, blank=True)
    capital = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES, null=True, blank=True)
    conquest = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES, null=True, blank=True)
    assassination = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES, null=True, blank=True)
    depose = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES, null=True, blank=True)
    constitution = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES, null=True, blank=True)
    labor = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES, null=True, blank=True)
    unfree_labor = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES, null=True, blank=True)
    suffrage = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES, null=True, blank=True)
    public_goods = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES, null=True, blank=True)
    religion = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES, null=True, blank=True)


    class Meta:
        verbose_name = 'Crisis consequence'
        verbose_name_plural = 'Crisis consequences'
        ordering = ['year_from', 'year_to']


    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "crisis_consequence"
    
    def get_columns_with_value(self, value):
        columns = []
        fields = ['decline', 'collapse', 'epidemic', 'downward_mobility', 'extermination', 'uprising', 'revolution', 'successful_revolution', 'civil_war', 'century_plus', 'fragmentation', 'capital', 'conquest', 'assassination', 'depose', 'constitution', 'labor', 'unfree_labor', 'suffrage', 'public_goods', 'religion']


        for field_name in fields:
            field_value = getattr(self, field_name)
            if field_value and field_value == value:
                columns.append(field_name)
        if columns != []:
            return columns
        else:
            return None

    def get_columns_with_value_dic(self, value):
        columns = {}
        fields = ['decline', 'collapse', 'epidemic', 'downward_mobility', 'extermination', 'uprising', 'revolution', 'successful_revolution', 'civil_war', 'century_plus', 'fragmentation', 'capital', 'conquest', 'assassination', 'depose', 'constitution', 'labor', 'unfree_labor', 'suffrage', 'public_goods', 'religion']
        from .custom_vars import crisis_defs_examples

        for field_name in fields:
            field_value = getattr(self, field_name)
            if field_value and field_value == value:
                columns[field_name] = crisis_defs_examples[field_name]
                
        if columns:
            return columns
        else:
            return None

    
    # def show_value(self):
    #     return self.get_human_sacrifice_display()
    
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name
        
    def clean_decline(self):
        return return_beautiful_abs_pres(self.decline)

    def clean_collapse(self):
        return return_beautiful_abs_pres(self.collapse)

    def get_absolute_url(self):
        return reverse('crisis_consequence-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)

########################################


class Power_transition(SeshatCommon):
    predecessor = models.CharField(max_length=200, blank=True, null=True)
    successor = models.CharField(max_length=200, blank=True,  null=True)
    reign_number_predecessor = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=400, blank=True,  null=True)
    culture_group = models.CharField(max_length=200, blank=True, null=True)


    contested = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES, blank=True,null=True)
    overturn = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES,  blank=True,null=True)
    predecessor_assassination = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES, blank=True,null=True)
    intra_elite = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES,  blank=True,null=True)
    military_revolt = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES,  blank=True,null=True)
    popular_uprising = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES,  blank=True,null=True)
    separatist_rebellion = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES,  blank=True,null=True)
    external_invasion = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES, blank=True,null=True)
    external_interference = models.CharField(max_length=5, choices=CRISIS_CONSEQUENCE_CHOICES, blank=True,null=True)

    class Meta:
        verbose_name = 'Power Transition'
        verbose_name_plural = 'Power Transitions'
        ordering = ['year_from', 'year_to']


    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "power_transition"
    
    def get_columns_with_value(self, value):
        columns = []
        fields = ['contested', 'overturn', 'predecessor_assassination', 'intra_elite', 'military_revolt', 'popular_uprising', 'separatist_rebellion', 'external_invasion', 'external_interference', ]


        for field_name in fields:
            field_value = getattr(self, field_name)
            if field_value and field_value == value:
                columns.append(field_name)
        if columns != []:
            return columns
        else:
            return None

    def get_columns_with_value_dic(self, value):
        columns = {}
        fields = ['contested', 'overturn', 'predecessor_assassination', 'intra_elite', 'military_revolt', 'popular_uprising', 'separatist_rebellion', 'external_invasion', 'external_interference', ]

        from .custom_vars import power_transitions_defs_examples

        for field_name in fields:
            field_value = getattr(self, field_name)
            if field_value and field_value == value:
                columns[field_name] = power_transitions_defs_examples[field_name]
                
        if columns:
            return columns
        else:
            return None
    
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('power_transition-detail', args=[str(self.id)])

    def __str__(self):
        if self.polity and self.predecessor and self.successor:
            return f"Power Transition in {self.polity}: {self.predecessor} was replaced by {self.successor}."
        else:
            return "Power Transition in x: Y was replaced by Z" 



########## Beginning of class Definitions for CrisisDB Models

class Human_sacrifice(SeshatCommon):
    name = models.CharField(max_length=100, default="Human_sacrifice")
    human_sacrifice = models.CharField(max_length=500, choices=HUMAN_SACRIFICE_HUMAN_SACRIFICE_CHOICES)



    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'human_sacrifice')
        verbose_name = 'Human_sacrifice'
        verbose_name_plural = 'Human_sacrifices'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "human_sacrifice"
    
    def show_value(self):
        return self.get_human_sacrifice_display()
    
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('human_sacrifice-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class External_conflict(SeshatCommon):
    name = models.CharField(max_length=100, default="External_conflict")
    conflict_name = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'conflict_name')
        verbose_name = 'External_conflict'
        verbose_name_plural = 'External_conflicts'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('external_conflict-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Internal_conflict(SeshatCommon):
    name = models.CharField(max_length=100, default="Internal_conflict")
    conflict = models.CharField(max_length=500, blank=True, null=True)
    expenditure = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)
    leader = models.CharField(max_length=500, blank=True, null=True)
    casualty = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'conflict', 'expenditure', 'leader', 'casualty')
        verbose_name = 'Internal_conflict'
        verbose_name_plural = 'Internal_conflicts'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('internal_conflict-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class External_conflict_side(SeshatCommon):
    name = models.CharField(max_length=100, default="External_conflict_side")
    conflict_id = models.ForeignKey(External_conflict, on_delete=models.SET_NULL, null=True, related_name="External_conflicts")
    expenditure = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)
    leader = models.CharField(max_length=500, blank=True, null=True)
    casualty = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'conflict_id', 'expenditure', 'leader', 'casualty')
        verbose_name = 'External_conflict_side'
        verbose_name_plural = 'External_conflict_sides'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('external_conflict_side-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Agricultural_population(SeshatCommon):
    name = models.CharField(max_length=100, default="Agricultural_population")
    agricultural_population = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'agricultural_population')
        verbose_name = 'Agricultural_population'
        verbose_name_plural = 'Agricultural_populations'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('agricultural_population-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Arable_land(SeshatCommon):
    name = models.CharField(max_length=100, default="Arable_land")
    arable_land = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'arable_land')
        verbose_name = 'Arable_land'
        verbose_name_plural = 'Arable_lands'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('arable_land-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Arable_land_per_farmer(SeshatCommon):
    name = models.CharField(max_length=100, default="Arable_land_per_farmer")
    arable_land_per_farmer = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'arable_land_per_farmer')
        verbose_name = 'Arable_land_per_farmer'
        verbose_name_plural = 'Arable_land_per_farmers'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('arable_land_per_farmer-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Gross_grain_shared_per_agricultural_population(SeshatCommon):
    name = models.CharField(max_length=100, default="Gross_grain_shared_per_agricultural_population")
    gross_grain_shared_per_agricultural_population = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'gross_grain_shared_per_agricultural_population')
        verbose_name = 'Gross_grain_shared_per_agricultural_population'
        verbose_name_plural = 'Gross_grain_shared_per_agricultural_populations'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('gross_grain_shared_per_agricultural_population-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Net_grain_shared_per_agricultural_population(SeshatCommon):
    name = models.CharField(max_length=100, default="Net_grain_shared_per_agricultural_population")
    net_grain_shared_per_agricultural_population = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'net_grain_shared_per_agricultural_population')
        verbose_name = 'Net_grain_shared_per_agricultural_population'
        verbose_name_plural = 'Net_grain_shared_per_agricultural_populations'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('net_grain_shared_per_agricultural_population-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Surplus(SeshatCommon):
    name = models.CharField(max_length=100, default="Surplus")
    surplus = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'surplus')
        verbose_name = 'Surplus'
        verbose_name_plural = 'Surplus'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('surplus-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Military_expense(SeshatCommon):
    name = models.CharField(max_length=100, default="Military_expense")
    conflict = models.CharField(max_length=500, blank=True, null=True)
    expenditure = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'conflict', 'expenditure')
        verbose_name = 'Military_expense'
        verbose_name_plural = 'Military_expenses'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('military_expense-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Silver_inflow(SeshatCommon):
    name = models.CharField(max_length=100, default="Silver_inflow")
    silver_inflow = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'silver_inflow')
        verbose_name = 'Silver_inflow'
        verbose_name_plural = 'Silver_inflows'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('silver_inflow-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Silver_stock(SeshatCommon):
    name = models.CharField(max_length=100, default="Silver_stock")
    silver_stock = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'silver_stock')
        verbose_name = 'Silver_stock'
        verbose_name_plural = 'Silver_stocks'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('silver_stock-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Total_population(SeshatCommon):
    name = models.CharField(max_length=100, default="Total_population")
    total_population = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'total_population')
        verbose_name = 'Total_population'
        verbose_name_plural = 'Total_populations'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('total_population-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Gdp_per_capita(SeshatCommon):
    name = models.CharField(max_length=100, default="Gdp_per_capita")
    gdp_per_capita = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'gdp_per_capita')
        verbose_name = 'Gdp_per_capita'
        verbose_name_plural = 'Gdp_per_capitas'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('gdp_per_capita-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Drought_event(SeshatCommon):
    name = models.CharField(max_length=100, default="Drought_event")
    drought_event = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'drought_event')
        verbose_name = 'Drought_event'
        verbose_name_plural = 'Drought_events'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('drought_event-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Locust_event(SeshatCommon):
    name = models.CharField(max_length=100, default="Locust_event")
    locust_event = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'locust_event')
        verbose_name = 'Locust_event'
        verbose_name_plural = 'Locust_events'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('locust_event-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Socioeconomic_turmoil_event(SeshatCommon):
    name = models.CharField(max_length=100, default="Socioeconomic_turmoil_event")
    socioeconomic_turmoil_event = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'socioeconomic_turmoil_event')
        verbose_name = 'Socioeconomic_turmoil_event'
        verbose_name_plural = 'Socioeconomic_turmoil_events'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('socioeconomic_turmoil_event-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Crop_failure_event(SeshatCommon):
    name = models.CharField(max_length=100, default="Crop_failure_event")
    crop_failure_event = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'crop_failure_event')
        verbose_name = 'Crop_failure_event'
        verbose_name_plural = 'Crop_failure_events'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('crop_failure_event-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Famine_event(SeshatCommon):
    name = models.CharField(max_length=100, default="Famine_event")
    famine_event = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'famine_event')
        verbose_name = 'Famine_event'
        verbose_name_plural = 'Famine_events'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('famine_event-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Disease_outbreak(SeshatCommon):
    name = models.CharField(max_length=100, default="Disease_outbreak")
    longitude = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)
    latitude = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)
    elevation = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)
    sub_category = models.CharField(max_length=500, choices=SUB_CATEGORY_DISEASE_OUTBREAK_CHOICES)
    magnitude = models.CharField(max_length=500, choices=MAGNITUDE_DISEASE_OUTBREAK_CHOICES)
    duration = models.CharField(max_length=500, choices=DURATION_DISEASE_OUTBREAK_CHOICES)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'longitude', 'latitude', 'elevation', 'sub_category', 'magnitude', 'duration')
        verbose_name = 'Disease_outbreak'
        verbose_name_plural = 'Disease_outbreaks'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('disease_outbreak-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
########## END of class Definitions for CrisisDB Models
