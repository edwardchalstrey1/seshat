
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
('A~P', 'Transitional (Absent -> Present)'),
('P~A', 'Transitional (Present -> Absent)'),
)




########## TUPLE CHOICES THAT ARE THE SAME 

########## END of tuple choices for general Models

########## Beginning of Function Definitions for Social Complexity (Vars) Models

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



    def show_value_from(self):
        if self.professional_military_officer:
            return self.professional_military_officer
        else:
            return None

    def show_value_to(self):
        return None  

########## End of Function Definitions for General (Vars) Models

########## Beginning of class Definitions for general Models

class Copper(SeshatCommon):
    name = models.CharField(max_length=100, default="Copper")
    copper = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Copper'
        verbose_name_plural = 'Coppers'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "copper"

    def clean_name_spaced(self):
        return "Copper"
    
    def show_value(self):
        if self.copper:
            return self.get_copper_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('copper-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Bronze(SeshatCommon):
    name = models.CharField(max_length=100, default="Bronze")
    bronze = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Bronze'
        verbose_name_plural = 'Bronzes'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "bronze"

    def clean_name_spaced(self):
        return "Bronze"
    
    def show_value(self):
        if self.bronze:
            return self.get_bronze_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('bronze-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Iron(SeshatCommon):
    name = models.CharField(max_length=100, default="Iron")
    iron = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Iron'
        verbose_name_plural = 'Irons'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "iron"

    def clean_name_spaced(self):
        return "Iron"
    
    def show_value(self):
        if self.iron:
            return self.get_iron_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('iron-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Steel(SeshatCommon):
    name = models.CharField(max_length=100, default="Steel")
    steel = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Steel'
        verbose_name_plural = 'Steels'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "steel"

    def clean_name_spaced(self):
        return "Steel"
    
    def show_value(self):
        if self.steel:
            return self.get_steel_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('steel-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Javelin(SeshatCommon):
    name = models.CharField(max_length=100, default="Javelin")
    javelin = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Javelin'
        verbose_name_plural = 'Javelins'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "javelin"

    def clean_name_spaced(self):
        return "Javelin"
    
    def show_value(self):
        if self.javelin:
            return self.get_javelin_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('javelin-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Atlatl(SeshatCommon):
    name = models.CharField(max_length=100, default="Atlatl")
    atlatl = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Atlatl'
        verbose_name_plural = 'Atlatls'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "atlatl"

    def clean_name_spaced(self):
        return "Atlatl"
    
    def show_value(self):
        if self.atlatl:
            return self.get_atlatl_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('atlatl-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Sling(SeshatCommon):
    name = models.CharField(max_length=100, default="Sling")
    sling = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Sling'
        verbose_name_plural = 'Slings'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "sling"

    def clean_name_spaced(self):
        return "Sling"
    
    def show_value(self):
        if self.sling:
            return self.get_sling_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('sling-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Self_bow(SeshatCommon):
    name = models.CharField(max_length=100, default="Self_bow")
    self_bow = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Self_bow'
        verbose_name_plural = 'Self_bows'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "self_bow"

    def clean_name_spaced(self):
        return "Self Bow"
    
    def show_value(self):
        if self.self_bow:
            return self.get_self_bow_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('self_bow-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Composite_bow(SeshatCommon):
    name = models.CharField(max_length=100, default="Composite_bow")
    composite_bow = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Composite_bow'
        verbose_name_plural = 'Composite_bows'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "composite_bow"

    def clean_name_spaced(self):
        return "Composite Bow"
    
    def show_value(self):
        if self.composite_bow:
            return self.get_composite_bow_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('composite_bow-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Crossbow(SeshatCommon):
    name = models.CharField(max_length=100, default="Crossbow")
    crossbow = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Crossbow'
        verbose_name_plural = 'Crossbows'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "crossbow"

    def clean_name_spaced(self):
        return "Crossbow"
    
    def show_value(self):
        if self.crossbow:
            return self.get_crossbow_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('crossbow-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Tension_siege_engine(SeshatCommon):
    name = models.CharField(max_length=100, default="Tension_siege_engine")
    tension_siege_engine = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Tension_siege_engine'
        verbose_name_plural = 'Tension_siege_engines'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "tension_siege_engine"

    def clean_name_spaced(self):
        return "Tension Siege Engine"
    
    def show_value(self):
        if self.tension_siege_engine:
            return self.get_tension_siege_engine_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('tension_siege_engine-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Sling_siege_engine(SeshatCommon):
    name = models.CharField(max_length=100, default="Sling_siege_engine")
    sling_siege_engine = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Sling_siege_engine'
        verbose_name_plural = 'Sling_siege_engines'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "sling_siege_engine"

    def clean_name_spaced(self):
        return "Sling Siege Engine"
    
    def show_value(self):
        if self.sling_siege_engine:
            return self.get_sling_siege_engine_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('sling_siege_engine-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Gunpowder_siege_artillery(SeshatCommon):
    name = models.CharField(max_length=100, default="Gunpowder_siege_artillery")
    gunpowder_siege_artillery = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Gunpowder_siege_artillery'
        verbose_name_plural = 'Gunpowder_siege_artilleries'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "gunpowder_siege_artillery"

    def clean_name_spaced(self):
        return "Gunpowder Siege Artillery"
    
    def show_value(self):
        if self.gunpowder_siege_artillery:
            return self.get_gunpowder_siege_artillery_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('gunpowder_siege_artillery-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Handheld_firearm(SeshatCommon):
    name = models.CharField(max_length=100, default="Handheld_firearm")
    handheld_firearm = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Handheld_firearm'
        verbose_name_plural = 'Handheld_firearms'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "handheld_firearm"

    def clean_name_spaced(self):
        return "Handheld Firearm"
    
    def show_value(self):
        if self.handheld_firearm:
            return self.get_handheld_firearm_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('handheld_firearm-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class War_club(SeshatCommon):
    name = models.CharField(max_length=100, default="War_club")
    war_club = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'War_club'
        verbose_name_plural = 'War_clubs'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "war_club"

    def clean_name_spaced(self):
        return "War Club"
    
    def show_value(self):
        if self.war_club:
            return self.get_war_club_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('war_club-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Battle_axe(SeshatCommon):
    name = models.CharField(max_length=100, default="Battle_axe")
    battle_axe = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Battle_axe'
        verbose_name_plural = 'Battle_axes'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "battle_axe"

    def clean_name_spaced(self):
        return "Battle Axe"
    
    def show_value(self):
        if self.battle_axe:
            return self.get_battle_axe_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('battle_axe-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Dagger(SeshatCommon):
    name = models.CharField(max_length=100, default="Dagger")
    dagger = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Dagger'
        verbose_name_plural = 'Daggers'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "dagger"

    def clean_name_spaced(self):
        return "Dagger"
    
    def show_value(self):
        if self.dagger:
            return self.get_dagger_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('dagger-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Sword(SeshatCommon):
    name = models.CharField(max_length=100, default="Sword")
    sword = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Sword'
        verbose_name_plural = 'Swords'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "sword"

    def clean_name_spaced(self):
        return "Sword"
    
    def show_value(self):
        if self.sword:
            return self.get_sword_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('sword-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Spear(SeshatCommon):
    name = models.CharField(max_length=100, default="Spear")
    spear = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Spear'
        verbose_name_plural = 'Spears'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "spear"

    def clean_name_spaced(self):
        return "Spear"
    
    def show_value(self):
        if self.spear:
            return self.get_spear_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('spear-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polearm(SeshatCommon):
    name = models.CharField(max_length=100, default="Polearm")
    polearm = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Polearm'
        verbose_name_plural = 'Polearms'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "polearm"

    def clean_name_spaced(self):
        return "Polearm"
    
    def show_value(self):
        if self.polearm:
            return self.get_polearm_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('polearm-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Dog(SeshatCommon):
    name = models.CharField(max_length=100, default="Dog")
    dog = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Dog'
        verbose_name_plural = 'Dogs'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "dog"

    def clean_name_spaced(self):
        return "Dog"
    
    def show_value(self):
        if self.dog:
            return self.get_dog_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('dog-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Donkey(SeshatCommon):
    name = models.CharField(max_length=100, default="Donkey")
    donkey = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Donkey'
        verbose_name_plural = 'Donkeies'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "donkey"

    def clean_name_spaced(self):
        return "Donkey"
    
    def show_value(self):
        if self.donkey:
            return self.get_donkey_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('donkey-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Horse(SeshatCommon):
    name = models.CharField(max_length=100, default="Horse")
    horse = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Horse'
        verbose_name_plural = 'Horses'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "horse"

    def clean_name_spaced(self):
        return "Horse"
    
    def show_value(self):
        if self.horse:
            return self.get_horse_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('horse-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Camel(SeshatCommon):
    name = models.CharField(max_length=100, default="Camel")
    camel = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Camel'
        verbose_name_plural = 'Camels'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "camel"

    def clean_name_spaced(self):
        return "Camel"
    
    def show_value(self):
        if self.camel:
            return self.get_camel_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('camel-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Elephant(SeshatCommon):
    name = models.CharField(max_length=100, default="Elephant")
    elephant = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Elephant'
        verbose_name_plural = 'Elephants'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "elephant"

    def clean_name_spaced(self):
        return "Elephant"
    
    def show_value(self):
        if self.elephant:
            return self.get_elephant_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('elephant-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Wood_bark_etc(SeshatCommon):
    name = models.CharField(max_length=100, default="Wood_bark_etc")
    wood_bark_etc = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Wood_bark_etc'
        verbose_name_plural = 'Wood_bark_etcs'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "wood_bark_etc"

    def clean_name_spaced(self):
        return "Wood Bark Etc"
    
    def show_value(self):
        if self.wood_bark_etc:
            return self.get_wood_bark_etc_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('wood_bark_etc-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Leather_cloth(SeshatCommon):
    name = models.CharField(max_length=100, default="Leather_cloth")
    leather_cloth = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Leather_cloth'
        verbose_name_plural = 'Leather_cloths'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "leather_cloth"

    def clean_name_spaced(self):
        return "Leather Cloth"
    
    def show_value(self):
        if self.leather_cloth:
            return self.get_leather_cloth_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('leather_cloth-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Shield(SeshatCommon):
    name = models.CharField(max_length=100, default="Shield")
    shield = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Shield'
        verbose_name_plural = 'Shields'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "shield"

    def clean_name_spaced(self):
        return "Shield"
    
    def show_value(self):
        if self.shield:
            return self.get_shield_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('shield-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Helmet(SeshatCommon):
    name = models.CharField(max_length=100, default="Helmet")
    helmet = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Helmet'
        verbose_name_plural = 'Helmets'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "helmet"

    def clean_name_spaced(self):
        return "Helmet"
    
    def show_value(self):
        if self.helmet:
            return self.get_helmet_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('helmet-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Breastplate(SeshatCommon):
    name = models.CharField(max_length=100, default="Breastplate")
    breastplate = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Breastplate'
        verbose_name_plural = 'Breastplates'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "breastplate"

    def clean_name_spaced(self):
        return "Breastplate"
    
    def show_value(self):
        if self.breastplate:
            return self.get_breastplate_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('breastplate-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Limb_protection(SeshatCommon):
    name = models.CharField(max_length=100, default="Limb_protection")
    limb_protection = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Limb_protection'
        verbose_name_plural = 'Limb_protections'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "limb_protection"

    def clean_name_spaced(self):
        return "Limb Protection"
    
    def show_value(self):
        if self.limb_protection:
            return self.get_limb_protection_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('limb_protection-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Scaled_armor(SeshatCommon):
    name = models.CharField(max_length=100, default="Scaled_armor")
    scaled_armor = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Scaled_armor'
        verbose_name_plural = 'Scaled_armors'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "scaled_armor"

    def clean_name_spaced(self):
        return "Scaled Armor"
    
    def show_value(self):
        if self.scaled_armor:
            return self.get_scaled_armor_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('scaled_armor-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Laminar_armor(SeshatCommon):
    name = models.CharField(max_length=100, default="Laminar_armor")
    laminar_armor = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Laminar_armor'
        verbose_name_plural = 'Laminar_armors'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "laminar_armor"

    def clean_name_spaced(self):
        return "Laminar Armor"
    
    def show_value(self):
        if self.laminar_armor:
            return self.get_laminar_armor_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('laminar_armor-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Plate_armor(SeshatCommon):
    name = models.CharField(max_length=100, default="Plate_armor")
    plate_armor = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Plate_armor'
        verbose_name_plural = 'Plate_armors'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "plate_armor"

    def clean_name_spaced(self):
        return "Plate Armor"
    
    def show_value(self):
        if self.plate_armor:
            return self.get_plate_armor_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('plate_armor-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Small_vessels_canoes_etc(SeshatCommon):
    name = models.CharField(max_length=100, default="Small_vessels_canoes_etc")
    small_vessels_canoes_etc = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Small_vessels_canoes_etc'
        verbose_name_plural = 'Small_vessels_canoes_etcs'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "small_vessels_canoes_etc"

    def clean_name_spaced(self):
        return "Small Vessels Canoes Etc"
    
    def show_value(self):
        if self.small_vessels_canoes_etc:
            return self.get_small_vessels_canoes_etc_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('small_vessels_canoes_etc-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Merchant_ships_pressed_into_service(SeshatCommon):
    name = models.CharField(max_length=100, default="Merchant_ships_pressed_into_service")
    merchant_ships_pressed_into_service = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Merchant_ships_pressed_into_service'
        verbose_name_plural = 'Merchant_ships_pressed_into_services'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "merchant_ships_pressed_into_service"

    def clean_name_spaced(self):
        return "Merchant Ships Pressed Into Service"
    
    def show_value(self):
        if self.merchant_ships_pressed_into_service:
            return self.get_merchant_ships_pressed_into_service_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('merchant_ships_pressed_into_service-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Specialized_military_vessel(SeshatCommon):
    name = models.CharField(max_length=100, default="Specialized_military_vessel")
    specialized_military_vessel = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Specialized_military_vessel'
        verbose_name_plural = 'Specialized_military_vessels'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "specialized_military_vessel"

    def clean_name_spaced(self):
        return "Specialized Military Vessel"
    
    def show_value(self):
        if self.specialized_military_vessel:
            return self.get_specialized_military_vessel_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('specialized_military_vessel-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Settlements_in_a_defensive_position(SeshatCommon):
    name = models.CharField(max_length=100, default="Settlements_in_a_defensive_position")
    settlements_in_a_defensive_position = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Settlements_in_a_defensive_position'
        verbose_name_plural = 'Settlements_in_a_defensive_positions'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "settlements_in_a_defensive_position"

    def clean_name_spaced(self):
        return "Settlements in a Defensive Position"
    
    def show_value(self):
        if self.settlements_in_a_defensive_position:
            return self.get_settlements_in_a_defensive_position_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('settlements_in_a_defensive_position-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Wooden_palisade(SeshatCommon):
    name = models.CharField(max_length=100, default="Wooden_palisade")
    wooden_palisade = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Wooden_palisade'
        verbose_name_plural = 'Wooden_palisades'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "wooden_palisade"

    def clean_name_spaced(self):
        return "Wooden Palisade"
    
    def show_value(self):
        if self.wooden_palisade:
            return self.get_wooden_palisade_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('wooden_palisade-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Earth_rampart(SeshatCommon):
    name = models.CharField(max_length=100, default="Earth_rampart")
    earth_rampart = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Earth_rampart'
        verbose_name_plural = 'Earth_ramparts'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "earth_rampart"

    def clean_name_spaced(self):
        return "Earth Rampart"
    
    def show_value(self):
        if self.earth_rampart:
            return self.get_earth_rampart_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('earth_rampart-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Ditch(SeshatCommon):
    name = models.CharField(max_length=100, default="Ditch")
    ditch = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Ditch'
        verbose_name_plural = 'Ditchs'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "ditch"

    def clean_name_spaced(self):
        return "Ditch"
    
    def show_value(self):
        if self.ditch:
            return self.get_ditch_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('ditch-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Moat(SeshatCommon):
    name = models.CharField(max_length=100, default="Moat")
    moat = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Moat'
        verbose_name_plural = 'Moats'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "moat"

    def clean_name_spaced(self):
        return "Moat"
    
    def show_value(self):
        if self.moat:
            return self.get_moat_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('moat-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Stone_walls_non_mortared(SeshatCommon):
    name = models.CharField(max_length=100, default="Stone_walls_non_mortared")
    stone_walls_non_mortared = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Stone_walls_non_mortared'
        verbose_name_plural = 'Stone_walls_non_mortareds'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "stone_walls_non_mortared"

    def clean_name_spaced(self):
        return "Stone Walls Non Mortared"
    
    def show_value(self):
        if self.stone_walls_non_mortared:
            return self.get_stone_walls_non_mortared_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('stone_walls_non_mortared-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Stone_walls_mortared(SeshatCommon):
    name = models.CharField(max_length=100, default="Stone_walls_mortared")
    stone_walls_mortared = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Stone_walls_mortared'
        verbose_name_plural = 'Stone_walls_mortareds'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "stone_walls_mortared"

    def clean_name_spaced(self):
        return "Stone Walls Mortared"
    
    def show_value(self):
        if self.stone_walls_mortared:
            return self.get_stone_walls_mortared_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('stone_walls_mortared-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Fortified_camp(SeshatCommon):
    name = models.CharField(max_length=100, default="Fortified_camp")
    fortified_camp = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Fortified_camp'
        verbose_name_plural = 'Fortified_camps'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "fortified_camp"

    def clean_name_spaced(self):
        return "Fortified Camp"
    
    def show_value(self):
        if self.fortified_camp:
            return self.get_fortified_camp_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('fortified_camp-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Complex_fortification(SeshatCommon):
    name = models.CharField(max_length=100, default="Complex_fortification")
    complex_fortification = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Complex_fortification'
        verbose_name_plural = 'Complex_fortifications'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "complex_fortification"

    def clean_name_spaced(self):
        return "Complex Fortification"
    
    def show_value(self):
        if self.complex_fortification:
            return self.get_complex_fortification_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('complex_fortification-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Modern_fortification(SeshatCommon):
    name = models.CharField(max_length=100, default="Modern_fortification")
    modern_fortification = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Modern_fortification'
        verbose_name_plural = 'Modern_fortifications'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "modern_fortification"

    def clean_name_spaced(self):
        return "Modern Fortification"
    
    def show_value(self):
        if self.modern_fortification:
            return self.get_modern_fortification_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('modern_fortification-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Chainmail(SeshatCommon):
    name = models.CharField(max_length=100, default="Chainmail")
    chainmail = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        verbose_name = 'Chainmail'
        verbose_name_plural = 'Chainmails'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def clean_name(self):
        return "chainmail"

    def clean_name_spaced(self):
        return "Chainmail"
    
    def show_value(self):
        if self.chainmail:
            return self.get_chainmail_display()
        else:
            return " - "
        
    def show_nga(self):
        nga_rel =  self.polity.polity_sides.first()
        if not nga_rel:
            return "NO_NGA_ASSOCIATED"
        else:
            return nga_rel.nga_party.name

    def get_absolute_url(self):
        return reverse('chainmail-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
########## END of class Definitions for general Models
