
########## Beginning of Model Imports
from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
#from model_utils.models import StatusModel
from django.core.exceptions import ValidationError
from django.urls import reverse

from datetime import date

import uuid

from django.utils import translation

from ..core.models import SeshatCommon, Certainty, Tags, Section, Subsection
from seshat.apps.accounts.models import Seshat_Expert


########## End of Model Imports

########## Beginning of tuple choices for general Models
ABSENT_PRESENT_CHOICES = (
('present', 'present'),
('absent', 'absent'),
('unknown', 'unknown'),
)


########## TUPLE CHOICES THAT ARE THE SAME 

########## END of tuple choices for general Models

########## Beginning of Function Definitions for General (Vars) Models

def call_my_name(self):
    if self.year_from == self.year_to or ((not self.year_to) and self.year_from):
        return self.name + " [for " + self.polity.name + " in " + str(self.year_from) + "]"
    else:
        return self.name + " [for " + self.polity.name + " from " + str(self.year_from) + " to " + str(self.year_to) + "]"


def return_citations(self):
    return ', '.join(['<a href="' + citation.zoteroer() + '">' + citation.__str__() + ' </a>' for citation in self.citations.all()[:2]])


def clean_times(self):
    if (self.year_from and self.year_to) and self.year_from > self.year_to:
        raise ValidationError({
            'year_from': 'The start year is bigger than the end year!',
        })
    if self.year_from and (self.year_from < -10000 or self.year_from > date.today().year):
        raise ValidationError({
            'year_from': 'The start year is out of range!',
        })
    if self.year_from and (self.year_from < self.polity.start_year):
        raise ValidationError({
            'year_from': 'The start year is earlier than the start year of the corresponding polity!',
        })
    if self.year_to and (self.year_to > self.polity.end_year):
        raise ValidationError({
            'year_to': 'The end year is later than the end year of the corresponding polity!',
        })
    if self.year_to and (self.year_to < -10000 or self.year_to > date.today().year):
        raise ValidationError({
            'year_to': 'The end year is out of range!',
        })
    if not self.year_to and not self.year_from:
        raise ValidationError({
            'year_from': 'You need to enter at least one year (From or To)',
        })

########## End of Function Definitions for General (Vars) Models

########## Beginning of class Definitions for general Models

class Ra(SeshatCommon):
    name = models.CharField(max_length=100, default="Ra")
    sc_ra = models.ForeignKey(Seshat_Expert, on_delete=models.SET_NULL, null=True, related_name="sc_research_assistant")

    class Meta:
        verbose_name = 'Ra'
        verbose_name_plural = 'Ras'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "ra"

    def clean_name_spaced(self):
        return "ra"
    
    def show_value(self):
        if self.sc_ra:
            return self.sc_ra
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('ra-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_territory(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_territory")
    polity_territory_from = models.IntegerField(blank=True, null=True)
    polity_territory_to = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Polity_territory'
        verbose_name_plural = 'Polity_territories'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "polity_territory"

    def clean_name_spaced(self):
        return "Polity Territory"
    
    def show_value(self):
        if self.polity_territory_from and self.polity_territory_to and self.polity_territory_to == self.polity_territory_from:
            return self.polity_territory_from
        elif self.polity_territory_from and self.polity_territory_to:
            return f"[{self.polity_territory_from:,} to {self.polity_territory_to:,}]"
        elif self.polity_territory_from:
            return f"[{self.polity_territory_from:,}"
        elif self.polity_territory_to:
            return f"[{self.polity_territory_to:,}"
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('polity_territory-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_population(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_population")
    polity_population_from = models.IntegerField(blank=True, null=True)
    polity_population_to = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Polity_population'
        verbose_name_plural = 'Polity_populations'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "polity_population"

    def clean_name_spaced(self):
        return "Polity Population"
    
    def show_value(self):
        if self.polity_population_from and self.polity_population_to and self.polity_population_to == self.polity_population_from:
            return self.polity_population_from
        elif self.polity_population_from and self.polity_population_to:
            return f"[{self.polity_population_from:,} to {self.polity_population_to:,}]"
        elif self.polity_population_from:
            return f"[{self.polity_population_from:,}"
        elif self.polity_population_to:
            return f"[{self.polity_population_to:,}"
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('polity_population-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Population_of_the_largest_settlement(SeshatCommon):
    name = models.CharField(max_length=100, default="Population_of_the_largest_settlement")
    population_of_the_largest_settlement_from = models.IntegerField(blank=True, null=True)
    population_of_the_largest_settlement_to = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Population_of_the_largest_settlement'
        verbose_name_plural = 'Population_of_the_largest_settlements'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "population_of_the_largest_settlement"

    def clean_name_spaced(self):
        return "Population of the Largest Settlement"
    
    def show_value(self):
        if self.population_of_the_largest_settlement_from and self.population_of_the_largest_settlement_to and self.population_of_the_largest_settlement_to == self.population_of_the_largest_settlement_from:
            return self.population_of_the_largest_settlement_from
        elif self.population_of_the_largest_settlement_from and self.population_of_the_largest_settlement_to:
            return f"[{self.population_of_the_largest_settlement_from:,} to {self.population_of_the_largest_settlement_to:,}]"
        elif self.population_of_the_largest_settlement_from:
            return f"[{self.population_of_the_largest_settlement_from:,}"
        elif self.population_of_the_largest_settlement_to:
            return f"[{self.population_of_the_largest_settlement_to:,}"
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('population_of_the_largest_settlement-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Settlement_hierarchy(SeshatCommon):
    name = models.CharField(max_length=100, default="Settlement_hierarchy")
    settlement_hierarchy_from = models.IntegerField(blank=True, null=True)
    settlement_hierarchy_to = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Settlement_hierarchy'
        verbose_name_plural = 'Settlement_hierarchies'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "settlement_hierarchy"

    def clean_name_spaced(self):
        return "Settlement Hierarchy"
    
    def show_value(self):
        if self.settlement_hierarchy_from and self.settlement_hierarchy_to and self.settlement_hierarchy_to == self.settlement_hierarchy_from:
            return self.settlement_hierarchy_from
        elif self.settlement_hierarchy_from and self.settlement_hierarchy_to:
            return f"[{self.settlement_hierarchy_from:,} to {self.settlement_hierarchy_to:,}]"
        elif self.settlement_hierarchy_from:
            return f"[{self.settlement_hierarchy_from:,}"
        elif self.settlement_hierarchy_to:
            return f"[{self.settlement_hierarchy_to:,}"
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('settlement_hierarchy-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Administrative_level(SeshatCommon):
    name = models.CharField(max_length=100, default="Administrative_level")
    administrative_level_from = models.IntegerField(blank=True, null=True)
    administrative_level_to = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Administrative_level'
        verbose_name_plural = 'Administrative_levels'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "administrative_level"

    def clean_name_spaced(self):
        return "Administrative Level"
    
    def show_value(self):
        if self.administrative_level_from and self.administrative_level_to and self.administrative_level_to == self.administrative_level_from:
            return self.administrative_level_from
        elif self.administrative_level_from and self.administrative_level_to:
            return f"[{self.administrative_level_from:,} to {self.administrative_level_to:,}]"
        elif self.administrative_level_from:
            return f"[{self.administrative_level_from:,}"
        elif self.administrative_level_to:
            return f"[{self.administrative_level_to:,}"
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('administrative_level-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Religious_level(SeshatCommon):
    name = models.CharField(max_length=100, default="Religious_level")
    religious_level_from = models.IntegerField(blank=True, null=True)
    religious_level_to = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Religious_level'
        verbose_name_plural = 'Religious_levels'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "religious_level"

    def clean_name_spaced(self):
        return "Religious Level"
    
    def show_value(self):
        if self.religious_level_from and self.religious_level_to and self.religious_level_to == self.religious_level_from:
            return self.religious_level_from
        elif self.religious_level_from and self.religious_level_to:
            return f"[{self.religious_level_from:,} to {self.religious_level_to:,}]"
        elif self.religious_level_from:
            return f"[{self.religious_level_from:,}"
        elif self.religious_level_to:
            return f"[{self.religious_level_to:,}"
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('religious_level-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Military_level(SeshatCommon):
    name = models.CharField(max_length=100, default="Military_level")
    military_level_from = models.IntegerField(blank=True, null=True)
    military_level_to = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Military_level'
        verbose_name_plural = 'Military_levels'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "military_level"

    def clean_name_spaced(self):
        return "Military Level"
    
    def show_value(self):
        if self.military_level_from and self.military_level_to and self.military_level_to == self.military_level_from:
            return self.military_level_from
        elif self.military_level_from and self.military_level_to:
            return f"[{self.military_level_from:,} to {self.military_level_to:,}]"
        elif self.military_level_from:
            return f"[{self.military_level_from:,}"
        elif self.military_level_to:
            return f"[{self.military_level_to:,}"
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('military_level-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Professional_military_officer(SeshatCommon):
    name = models.CharField(max_length=100, default="Professional_military_officer")
    professional_military_officer = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Professional_military_officer'
        verbose_name_plural = 'Professional_military_officers'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "professional_military_officer"

    def clean_name_spaced(self):
        return "Professional Military Officer"
    
    def show_value(self):
        if self.professional_military_officer:
            return self.get_professional_military_officer_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('professional_military_officer-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Professional_soldier(SeshatCommon):
    name = models.CharField(max_length=100, default="Professional_soldier")
    professional_soldier = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Professional_soldier'
        verbose_name_plural = 'Professional_soldiers'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "professional_soldier"

    def clean_name_spaced(self):
        return "Professional Soldier"
    
    def show_value(self):
        if self.professional_soldier:
            return self.get_professional_soldier_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('professional_soldier-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Professional_priesthood(SeshatCommon):
    name = models.CharField(max_length=100, default="Professional_priesthood")
    professional_priesthood = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Professional_priesthood'
        verbose_name_plural = 'Professional_priesthoods'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "professional_priesthood"

    def clean_name_spaced(self):
        return "Professional Priesthood"
    
    def show_value(self):
        if self.professional_priesthood:
            return self.get_professional_priesthood_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('professional_priesthood-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Full_time_bureaucrat(SeshatCommon):
    name = models.CharField(max_length=100, default="Full_time_bureaucrat")
    full_time_bureaucrat = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Full_time_bureaucrat'
        verbose_name_plural = 'Full_time_bureaucrats'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "full_time_bureaucrat"

    def clean_name_spaced(self):
        return "Full Time Bureaucrat"
    
    def show_value(self):
        if self.full_time_bureaucrat:
            return self.get_full_time_bureaucrat_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('full_time_bureaucrat-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Examination_system(SeshatCommon):
    name = models.CharField(max_length=100, default="Examination_system")
    examination_system = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Examination_system'
        verbose_name_plural = 'Examination_systems'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "examination_system"

    def clean_name_spaced(self):
        return "Examination System"
    
    def show_value(self):
        if self.examination_system:
            return self.get_examination_system_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('examination_system-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Merit_promotion(SeshatCommon):
    name = models.CharField(max_length=100, default="Merit_promotion")
    merit_promotion = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Merit_promotion'
        verbose_name_plural = 'Merit_promotions'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "merit_promotion"

    def clean_name_spaced(self):
        return "Merit Promotion"
    
    def show_value(self):
        if self.merit_promotion:
            return self.get_merit_promotion_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('merit_promotion-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Specialized_government_building(SeshatCommon):
    name = models.CharField(max_length=100, default="Specialized_government_building")
    specialized_government_building = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Specialized_government_building'
        verbose_name_plural = 'Specialized_government_buildings'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "specialized_government_building"

    def clean_name_spaced(self):
        return "Specialized Government Building"
    
    def show_value(self):
        if self.specialized_government_building:
            return self.get_specialized_government_building_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('specialized_government_building-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Formal_legal_code(SeshatCommon):
    name = models.CharField(max_length=100, default="Formal_legal_code")
    formal_legal_code = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Formal_legal_code'
        verbose_name_plural = 'Formal_legal_codes'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "formal_legal_code"

    def clean_name_spaced(self):
        return "Formal Legal Code"
    
    def show_value(self):
        if self.formal_legal_code:
            return self.get_formal_legal_code_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('formal_legal_code-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Judge(SeshatCommon):
    name = models.CharField(max_length=100, default="Judge")
    judge = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Judge'
        verbose_name_plural = 'Judges'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "judge"

    def clean_name_spaced(self):
        return "Judge"
    
    def show_value(self):
        if self.judge:
            return self.get_judge_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('judge-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Court(SeshatCommon):
    name = models.CharField(max_length=100, default="Court")
    court = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Court'
        verbose_name_plural = 'Courts'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "court"

    def clean_name_spaced(self):
        return "Court"
    
    def show_value(self):
        if self.court:
            return self.get_court_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('court-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Professional_lawyer(SeshatCommon):
    name = models.CharField(max_length=100, default="Professional_lawyer")
    professional_lawyer = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Professional_lawyer'
        verbose_name_plural = 'Professional_lawyers'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "professional_lawyer"

    def clean_name_spaced(self):
        return "Professional Lawyer"
    
    def show_value(self):
        if self.professional_lawyer:
            return self.get_professional_lawyer_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('professional_lawyer-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Irrigation_system(SeshatCommon):
    name = models.CharField(max_length=100, default="Irrigation_system")
    irrigation_system = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Irrigation_system'
        verbose_name_plural = 'Irrigation_systems'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "irrigation_system"

    def clean_name_spaced(self):
        return "Irrigation System"
    
    def show_value(self):
        if self.irrigation_system:
            return self.get_irrigation_system_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('irrigation_system-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Drinking_water_supply_system(SeshatCommon):
    name = models.CharField(max_length=100, default="Drinking_water_supply_system")
    drinking_water_supply_system = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Drinking_water_supply_system'
        verbose_name_plural = 'Drinking_water_supply_systems'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "drinking_water_supply_system"

    def clean_name_spaced(self):
        return "Drinking Water Supply System"
    
    def show_value(self):
        if self.drinking_water_supply_system:
            return self.get_drinking_water_supply_system_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('drinking_water_supply_system-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Market(SeshatCommon):
    name = models.CharField(max_length=100, default="Market")
    market = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Market'
        verbose_name_plural = 'Markets'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "market"

    def clean_name_spaced(self):
        return "Market"
    
    def show_value(self):
        if self.market:
            return self.get_market_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('market-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Food_storage_site(SeshatCommon):
    name = models.CharField(max_length=100, default="Food_storage_site")
    food_storage_site = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Food_storage_site'
        verbose_name_plural = 'Food_storage_sites'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "food_storage_site"

    def clean_name_spaced(self):
        return "Food Storage Site"
    
    def show_value(self):
        if self.food_storage_site:
            return self.get_food_storage_site_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('food_storage_site-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Road(SeshatCommon):
    name = models.CharField(max_length=100, default="Road")
    road = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Road'
        verbose_name_plural = 'Roads'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "road"

    def clean_name_spaced(self):
        return "Road"
    
    def show_value(self):
        if self.road:
            return self.get_road_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('road-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Bridge(SeshatCommon):
    name = models.CharField(max_length=100, default="Bridge")
    bridge = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Bridge'
        verbose_name_plural = 'Bridges'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "bridge"

    def clean_name_spaced(self):
        return "Bridge"
    
    def show_value(self):
        if self.bridge:
            return self.get_bridge_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('bridge-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Canal(SeshatCommon):
    name = models.CharField(max_length=100, default="Canal")
    canal = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Canal'
        verbose_name_plural = 'Canals'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "canal"

    def clean_name_spaced(self):
        return "Canal"
    
    def show_value(self):
        if self.canal:
            return self.get_canal_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('canal-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Port(SeshatCommon):
    name = models.CharField(max_length=100, default="Port")
    port = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Port'
        verbose_name_plural = 'Ports'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "port"

    def clean_name_spaced(self):
        return "Port"
    
    def show_value(self):
        if self.port:
            return self.get_port_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('port-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Mines_or_quarry(SeshatCommon):
    name = models.CharField(max_length=100, default="Mines_or_quarry")
    mines_or_quarry = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Mines_or_quarry'
        verbose_name_plural = 'Mines_or_quarries'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "mines_or_quarry"

    def clean_name_spaced(self):
        return "Mines or Quarry"
    
    def show_value(self):
        if self.mines_or_quarry:
            return self.get_mines_or_quarry_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('mines_or_quarry-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Mnemonic_device(SeshatCommon):
    name = models.CharField(max_length=100, default="Mnemonic_device")
    mnemonic_device = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Mnemonic_device'
        verbose_name_plural = 'Mnemonic_devices'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "mnemonic_device"

    def clean_name_spaced(self):
        return "Mnemonic Device"
    
    def show_value(self):
        if self.mnemonic_device:
            return self.get_mnemonic_device_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('mnemonic_device-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Nonwritten_record(SeshatCommon):
    name = models.CharField(max_length=100, default="Nonwritten_record")
    nonwritten_record = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Nonwritten_record'
        verbose_name_plural = 'Nonwritten_records'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "nonwritten_record"

    def clean_name_spaced(self):
        return "Nonwritten Record"
    
    def show_value(self):
        if self.nonwritten_record:
            return self.get_nonwritten_record_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('nonwritten_record-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Written_record(SeshatCommon):
    name = models.CharField(max_length=100, default="Written_record")
    written_record = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Written_record'
        verbose_name_plural = 'Written_records'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "written_record"

    def clean_name_spaced(self):
        return "Written Record"
    
    def show_value(self):
        if self.written_record:
            return self.get_written_record_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('written_record-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Script(SeshatCommon):
    name = models.CharField(max_length=100, default="Script")
    script = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Script'
        verbose_name_plural = 'Scripts'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "script"

    def clean_name_spaced(self):
        return "Script"
    
    def show_value(self):
        if self.script:
            return self.get_script_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('script-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Non_phonetic_writing(SeshatCommon):
    name = models.CharField(max_length=100, default="Non_phonetic_writing")
    non_phonetic_writing = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Non_phonetic_writing'
        verbose_name_plural = 'Non_phonetic_writings'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "non_phonetic_writing"

    def clean_name_spaced(self):
        return "Non Phonetic Writing"
    
    def show_value(self):
        if self.non_phonetic_writing:
            return self.get_non_phonetic_writing_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('non_phonetic_writing-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Phonetic_alphabetic_writing(SeshatCommon):
    name = models.CharField(max_length=100, default="Phonetic_alphabetic_writing")
    phonetic_alphabetic_writing = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Phonetic_alphabetic_writing'
        verbose_name_plural = 'Phonetic_alphabetic_writings'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "phonetic_alphabetic_writing"

    def clean_name_spaced(self):
        return "Phonetic Alphabetic Writing"
    
    def show_value(self):
        if self.phonetic_alphabetic_writing:
            return self.get_phonetic_alphabetic_writing_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('phonetic_alphabetic_writing-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Lists_tables_and_classification(SeshatCommon):
    name = models.CharField(max_length=100, default="Lists_tables_and_classification")
    lists_tables_and_classification = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Lists_tables_and_classification'
        verbose_name_plural = 'Lists_tables_and_classifications'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "lists_tables_and_classification"

    def clean_name_spaced(self):
        return "Lists Tables and Classification"
    
    def show_value(self):
        if self.lists_tables_and_classification:
            return self.get_lists_tables_and_classification_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('lists_tables_and_classification-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Calendar(SeshatCommon):
    name = models.CharField(max_length=100, default="Calendar")
    calendar = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Calendar'
        verbose_name_plural = 'Calendars'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "calendar"

    def clean_name_spaced(self):
        return "Calendar"
    
    def show_value(self):
        if self.calendar:
            return self.get_calendar_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('calendar-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Sacred_text(SeshatCommon):
    name = models.CharField(max_length=100, default="Sacred_text")
    sacred_text = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Sacred_text'
        verbose_name_plural = 'Sacred_texts'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "sacred_text"

    def clean_name_spaced(self):
        return "Sacred Text"
    
    def show_value(self):
        if self.sacred_text:
            return self.get_sacred_text_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('sacred_text-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Religious_literature(SeshatCommon):
    name = models.CharField(max_length=100, default="Religious_literature")
    religious_literature = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Religious_literature'
        verbose_name_plural = 'Religious_literatures'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "religious_literature"

    def clean_name_spaced(self):
        return "Religious Literature"
    
    def show_value(self):
        if self.religious_literature:
            return self.get_religious_literature_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('religious_literature-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Practical_literature(SeshatCommon):
    name = models.CharField(max_length=100, default="Practical_literature")
    practical_literature = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Practical_literature'
        verbose_name_plural = 'Practical_literatures'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "practical_literature"

    def clean_name_spaced(self):
        return "Practical Literature"
    
    def show_value(self):
        if self.practical_literature:
            return self.get_practical_literature_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('practical_literature-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class History(SeshatCommon):
    name = models.CharField(max_length=100, default="History")
    history = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'History'
        verbose_name_plural = 'Histories'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "history"

    def clean_name_spaced(self):
        return "History"
    
    def show_value(self):
        if self.history:
            return self.get_history_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('history-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Philosophy(SeshatCommon):
    name = models.CharField(max_length=100, default="Philosophy")
    philosophy = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Philosophy'
        verbose_name_plural = 'Philosophies'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "philosophy"

    def clean_name_spaced(self):
        return "Philosophy"
    
    def show_value(self):
        if self.philosophy:
            return self.get_philosophy_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('philosophy-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Scientific_literature(SeshatCommon):
    name = models.CharField(max_length=100, default="Scientific_literature")
    scientific_literature = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Scientific_literature'
        verbose_name_plural = 'Scientific_literatures'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "scientific_literature"

    def clean_name_spaced(self):
        return "Scientific Literature"
    
    def show_value(self):
        if self.scientific_literature:
            return self.get_scientific_literature_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('scientific_literature-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Fiction(SeshatCommon):
    name = models.CharField(max_length=100, default="Fiction")
    fiction = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Fiction'
        verbose_name_plural = 'Fictions'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "fiction"

    def clean_name_spaced(self):
        return "Fiction"
    
    def show_value(self):
        if self.fiction:
            return self.get_fiction_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('fiction-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Article(SeshatCommon):
    name = models.CharField(max_length=100, default="Article")
    article = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "article"

    def clean_name_spaced(self):
        return "Article"
    
    def show_value(self):
        if self.article:
            return self.get_article_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Token(SeshatCommon):
    name = models.CharField(max_length=100, default="Token")
    token = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Token'
        verbose_name_plural = 'Tokens'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "token"

    def clean_name_spaced(self):
        return "Token"
    
    def show_value(self):
        if self.token:
            return self.get_token_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('token-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Precious_metal(SeshatCommon):
    name = models.CharField(max_length=100, default="Precious_metal")
    precious_metal = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Precious_metal'
        verbose_name_plural = 'Precious_metals'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "precious_metal"

    def clean_name_spaced(self):
        return "Precious Metal"
    
    def show_value(self):
        if self.precious_metal:
            return self.get_precious_metal_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('precious_metal-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Foreign_coin(SeshatCommon):
    name = models.CharField(max_length=100, default="Foreign_coin")
    foreign_coin = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Foreign_coin'
        verbose_name_plural = 'Foreign_coins'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "foreign_coin"

    def clean_name_spaced(self):
        return "Foreign Coin"
    
    def show_value(self):
        if self.foreign_coin:
            return self.get_foreign_coin_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('foreign_coin-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Indigenous_coin(SeshatCommon):
    name = models.CharField(max_length=100, default="Indigenous_coin")
    indigenous_coin = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Indigenous_coin'
        verbose_name_plural = 'Indigenous_coins'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "indigenous_coin"

    def clean_name_spaced(self):
        return "Indigenous Coin"
    
    def show_value(self):
        if self.indigenous_coin:
            return self.get_indigenous_coin_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('indigenous_coin-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Paper_currency(SeshatCommon):
    name = models.CharField(max_length=100, default="Paper_currency")
    paper_currency = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Paper_currency'
        verbose_name_plural = 'Paper_currencies'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "paper_currency"

    def clean_name_spaced(self):
        return "Paper Currency"
    
    def show_value(self):
        if self.paper_currency:
            return self.get_paper_currency_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('paper_currency-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Courier(SeshatCommon):
    name = models.CharField(max_length=100, default="Courier")
    courier = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Courier'
        verbose_name_plural = 'Couriers'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "courier"

    def clean_name_spaced(self):
        return "Courier"
    
    def show_value(self):
        if self.courier:
            return self.get_courier_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('courier-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Postal_station(SeshatCommon):
    name = models.CharField(max_length=100, default="Postal_station")
    postal_station = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Postal_station'
        verbose_name_plural = 'Postal_stations'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "postal_station"

    def clean_name_spaced(self):
        return "Postal Station"
    
    def show_value(self):
        if self.postal_station:
            return self.get_postal_station_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('postal_station-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class General_postal_service(SeshatCommon):
    name = models.CharField(max_length=100, default="General_postal_service")
    general_postal_service = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'General_postal_service'
        verbose_name_plural = 'General_postal_services'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "general_postal_service"

    def clean_name_spaced(self):
        return "General Postal Service"
    
    def show_value(self):
        if self.general_postal_service:
            return self.get_general_postal_service_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        return reverse('general_postal_service-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
########## END of class Definitions for general Models
