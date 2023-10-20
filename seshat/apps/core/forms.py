from seshat.utils.utils import adder, dic_of_all_vars, list_of_all_Polities, dic_of_all_vars_in_sections

from django import forms
from django.forms import formset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from seshat.apps.core.models import Section, Subsection, Variablehierarchy, Reference, Citation, SeshatComment, SeshatCommentPart, Polity, Capital, Nga
from django.core.exceptions import NON_FIELD_ERRORS
from crispy_forms.helper import FormHelper

from django.core.exceptions import ValidationError


class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = ('title', 'year', 'creator', 'zotero_link', 'long_name')
        labels = {
        'title': '<b>title</b>',
        'year': '<b>Year</b>',
        'creator': '<b>Creator </b>',
        'zotero_link': '<b>zotero_link</b>',
        'long_name': '<b>Long Name</b>',
        }
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control mb-3', }),
            'year': forms.NumberInput(
                attrs={'class': 'form-control  mb-3 fw-bold', }),
            'creator': forms.TextInput(
                attrs={'class': 'form-control mb-3', }),
            'zotero_link': forms.TextInput(
                attrs={'class': 'form-control mb-3',}),
            'long_name': forms.Textarea(attrs={'class': 'form-control  mb-3', 'style': 'height: 100px',}),

        }


class CitationForm(forms.ModelForm):

    class Meta:
        model = Citation
        fields = ('ref', 'page_from', 'page_to', )
        labels = {
        'page_from': '<b>Start Page</b>',
        'page_to': '<b>End Page</b>',
        'ref': '<b>Select Your Reference: </b>',
        }
        widgets = {
            'ref': forms.Select(attrs={'class': 'form-control form-select mb-3 js-states js-example-basic-single', 'text':'ref' ,}),
            'page_from': forms.NumberInput(
            attrs={'class': 'form-control  mb-3 fw-bold', }),
            'page_to': forms.NumberInput(
            attrs={'class': 'form-control  mb-3 fw-bold', })
        }
    def clean(self):
        cleaned_data = super(CitationForm, self).clean()
        cleaned_page_from = cleaned_data.get("page_from")
        cleaned_page_to = cleaned_data.get("page_to")
        referenced_ref = cleaned_data.get("ref")
        #all_references = Reference.objects.all()
        all_citations =  Citation.objects.all()
        for a_citation in all_citations:
            if a_citation.ref.id == referenced_ref.id and cleaned_page_from == a_citation.page_from and a_citation.page_to == cleaned_page_to:
                print(f"PPPPPPPPPPPP : There is a citation with this info and it has the id: {str(a_citation.id)}", referenced_ref.id, referenced_ref.long_name)
                raise ValidationError("There is already a citation with the given information. We cannot create a duplicate.")
        #if not cleaned_page_from and not cleaned_page_to:
        #    raise ValidationError('Page to and from are empty. Bad.')
        return cleaned_data


class PolityForm(forms.ModelForm):
    class Meta:
        model = Polity
        fields = ('name', 'new_name', 'long_name', 'start_year', 'end_year', 'general_description')
        labels = {
        'name': 'Polity ID (Old)',
        'new_name': 'Polity ID (New)',
        'long_name': 'Long Name',
        'start_year': 'Start Year',
        'end_year': 'End Year',
        'general_description': 'General Description of the Polity',

        }
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control mb-3', }),
            'new_name': forms.TextInput(
                attrs={'class': 'form-control mb-3', }),
            'long_name': forms.TextInput(
                attrs={'class': 'form-control mb-3', }),
            'start_year': forms.NumberInput(
                attrs={'class': 'form-control  mb-3 fw-bold', }),
            'end_year': forms.NumberInput(
                attrs={'class': 'form-control  mb-3 fw-bold', }),
            'general_description': forms.Textarea(attrs={'class': 'form-control  mb-3', 'style': 'height: 300px', 'placeholder':'Add a general description (optional)'}),

        }

        
class NgaForm(forms.ModelForm):
    class Meta:
        model = Nga
        fields = ('name', 'world_region', 'subregion', 'fao_country')
        labels = {
        'name': '<b>NGA</b>',
        'world_region': '<b>World Region</b>',
        'subregion': '<b>Subregion</b>',
        'fao_country': '<b>Current Country</b>',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control mb-3', }),
            'world_region': forms.Select(attrs={'class': 'form-control form-select mb-3',}),
            'subregion': forms.TextInput(
                attrs={'class': 'form-control mb-3', }),
            'fao_country': forms.TextInput(
                attrs={'class': 'form-control mb-3', }),
        }


class CapitalForm(forms.ModelForm):
    class Meta:
        model = Capital
        fields = ('name', 'latitude', 'longitude', 'polity_cap', 'current_country', 'is_verified', 'url_on_the_map', 'note')
        labels = {
        'name': '<b>Capital</b>',
        'latitude': '<b>Latitude</b>',
        'longitude': '<b>Longitude</b>',
        'polity_cap': '<b>Polity</b>',
        'current_country': '<b>Current Country</b>',
        'is_verified': '<b class="text-primary">Verified?</b>',
        'url_on_the_map': '<b>Link on Google Maps</b>',
        'note': '<b>Add an optional Note</b>',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control mb-3', }),
            'polity_cap': forms.Select(attrs={'class': 'form-control form-select mb-3',}),
            'current_country': forms.TextInput(
                attrs={'class': 'form-control mb-3', }),
            'url_on_the_map': forms.Textarea(attrs={'class': 'form-control  mb-3', 'style': 'height: 120px', 'placeholder':'Add the full URL from Google Maps (optional)'}),
            'note': forms.Textarea(attrs={'class': 'form-control  mb-3', 'style': 'height: 120px', 'placeholder':'Add a note (optional)'}),
            'latitude': forms.NumberInput(
                attrs={'class': 'form-control  mb-3 fw-bold', }),
            'longitude': forms.NumberInput(
                attrs={'class': 'form-control  mb-3 fw-bold', }),
            'is_verified' : forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'form-control form-check-input mb-3'}),
            #'is_verified' : forms.Select(attrs={'class': 'form-control form-select mb-3',}),
        }


class SeshatCommentForm(forms.ModelForm):
    class Meta:
        model = SeshatComment
        fields = ('text',)
        labels = {
        'text': '<b>Description</b>',
        }
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control  mb-3', 'style': 'height: 100px',}),
        }

class SeshatCommentPartForm(forms.ModelForm):
    class Meta:
        model = SeshatCommentPart
        fields = ('comment', 'comment_part_text', 'comment_citations', 'comment_order', 'comment_curator')
        labels = {
        'comment': '<b>Description ID</b>',
        'comment_part_text': '<b>SubDescription Text</b>',
        'comment_citations': '<b>SubDescription Citations</b>',
        'comment_order': '<b>SubDescription Order in the Description:</b>',
        'comment_curator': '<b>Curator:</b>',
        }
        widgets = {
            'comment': forms.NumberInput(
                attrs={'class': 'form-control  mb-3 fw-bold', }),
            'comment_order': forms.NumberInput(
                attrs={'class': 'form-control  mb-3 fw-bold', }),
            'comment_part_text': forms.Textarea(attrs={'class': 'form-control  mb-3', 'style': 'height: 300px',}),
            'comment_citations': forms.SelectMultiple(attrs={'class': 'form-control mb-3 js-states js-example-basic-multiple', 'text':'citations[]' , 'style': 'height: 340px', 'multiple': 'multiple'}),
            'comment_curator': forms.Select(attrs={'class': 'form-control form-select mb-3',}),
        }


class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(
    #     max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(
    #     max_length=30, required=False, help_text='Optional.')
    # email = forms.EmailField(
    #     max_length=254, help_text='Required. Inform a valid email address.')
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'type': 'password', 'align': 'center', 'placeholder': 'password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'type': 'password', 'align': 'center', 'placeholder': 'password'}),
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            username, domain = email.split('@')
            username_parts = username.split('.')
            if len(username_parts) > 5:
                raise ValidationError("Email address contains too many dots in the username part.")
        return email

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control mb-3', }),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control mb-3', }),
            'username': forms.TextInput(
                attrs={'class': 'form-control mb-3', }),
            'email': forms.EmailInput(
                attrs={'class': 'form-control mb-3', }),
        }


# class VariablehierarchyForm(forms.ModelForm):
#     my_vars = dic_of_all_vars()
#     my_vars_tuple = [(key, key) for key in my_vars.keys()]
#     print(my_vars_tuple)
#     name = forms.ChoiceField(
#         label="Variable Name",
#         widget=forms.Select(attrs={'class': 'form-control  mb-3', }), choices=my_vars_tuple)

#     class Meta:
#         model = Variablehierarchy
#         fields = ('name', 'section', 'subsection')
#         widgets = {
#             'section': forms.Select(attrs={'class': 'form-control  mb-3', }),
#             'subsection': forms.Select(attrs={'class': 'form-control  mb-3', }),
#         }

class VariablehierarchyFormNew(forms.Form):
    my_vars = dic_of_all_vars()
    my_vars_tuple = [('', ' -- Select Variable -- ')]
    # print(my_vars_tuple)
    variable_name = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control form-select mb-3', 'name': "variable_name", 'id': "variable_name",}))
    section_name = forms.ChoiceField(
        label="Section",
        widget=forms.Select(attrs={'class': 'form-control form-select mb-3 required-entry',
                                'name': "section",
                                'id': "section",
                                'onchange': "javascript: dynamicdropdown(this.options[this.selectedIndex].value);"
                                }),)
    subsection_name = forms.ChoiceField(
        label="Subsection",
        widget=forms.Select(attrs={'class': 'form-control form-select mb-3',
                                'name': "subsection",
                                'id': "subsection", }),)
    # forms.CheckboxInput(attrs={'class': 'form-control mb-3', })
    is_verified = forms.BooleanField(
        label=" Verified?", required=False, widget=forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'form-control form-check-input align-middle'}))
    
    class Meta:
        unique_together = ("variable_name", "section_name", "subsection_name")

# VarHierFormSet = formset_factory(VariablehierarchyForm, extra=10)
