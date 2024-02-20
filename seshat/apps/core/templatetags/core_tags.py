from django import template
from django.db import connection
from django.db.models import F
from ..models import Polity, Capital
from ...general.models import Polity_capital
from ..views import get_polity_shape_content

register = template.Library()

@register.inclusion_tag('core/polity_map.html')
def polity_map(pk, tolerance='default'):
    """
        This function is used by the polity_map template and gets the specific polity shape data and capital information.
        Sets include_polity_map to False if there is no shape data.
        include_polity_map is used to determine whether to display the map on polity_detail.html.
    """
    page_id = str(pk)
    polity = Polity.objects.get(id=page_id)
    try:
        content = get_polity_shape_content(seshat_id=polity.new_name)
        # TODO: Temp commented out whilst polity start and end years don't match shape data
        # (see get_polity_shape_content() in views.py
        # content['earliest_year'] = polity.start_year
        # content['latest_year'] = polity.end_year
        # content['display_year'] = polity.start_year + round(((polity.end_year - polity.start_year) / 2))

        if tolerance == 'default':  # Used for testing
            capitals_info = get_polity_capitals(pk)
        else:
            capitals_info = get_polity_capitals(pk, polity_tolerance=tolerance)
        # Set the start and end years to be the same as the polity where missing
        modified_caps = capitals_info
        i = 0
        for capital_info in caps:
            if capital_info['year_from'] == None:
                modified_caps[i]['year_from'] = polity.start_year
            if capital_info['year_to'] == None:
                modified_caps[i]['year_to'] = polity.end_year
            i+=1
        content['capitals_info'] = modified_caps
        content['include_polity_map'] = True
    except:
        content = {}
        content['include_polity_map'] = False
    return {'content': content}

def get_polity_capitals(pk):
    """
        Get all the capitals for a polity and coordinates.
    """
    capitals_info = []
    polity_capitals = Polity_capital.objects.filter(polity_id=pk)
    
    for polity_capital in polity_capitals:
        capitals = Capital.objects.filter(name=polity_capital.capital)
        for capital in capitals:
            capital_info = {}
            if capital.name and capital.latitude and capital.longitude:
                capital_info['capital'] = capital.name
                capital_info['latitude'] = float(capital.latitude)
                capital_info['longitude'] = float(capital.longitude)

                if polity_capital.year_from == 0:
                    capital_info['year_from'] = 0
                elif polity_capital.year_from is not None:
                    capital_info['year_from'] = polity_capital.year_from
                else:
                    capital_info['year_from'] = None
                
                if polity_capital.year_to == 0:
                    capital_info['year_to'] = 0
                elif polity_capital.year_to is not None:
                    capital_info['year_to'] = polity_capital.year_to
                else:
                    capital_info['year_to'] = None
                
                capitals_info.append(capital_info)
    
    return capitals_info
