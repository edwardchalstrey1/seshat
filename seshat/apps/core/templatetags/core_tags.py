from django import template
from django.db import connection
from ..models import Polity
from ..views import get_polity_shape_content

register = template.Library()

@register.inclusion_tag('core/polity_map.html')
def polity_map(pk):
    page_id = str(pk)
    polity = Polity.objects.get(id=page_id)
    content = get_polity_shape_content(seshat_id=polity.new_name)
    content['earliest_year'] = polity.start_year
    content['latest_year'] = polity.end_year
    content['display_year'] = polity.start_year + round(((polity.end_year - polity.start_year) / 2))
    content['capitals_info'] = get_polity_capitals(pk)
    return {'content': content}

def get_polity_capitals(pk):
    query = """
            SELECT gpc.capital, CAST(cc.latitude AS FLOAT), CAST(cc.longitude AS FLOAT)
            FROM core_polity as cp, general_polity_capital as gpc, core_capital as cc
            WHERE cp.id = gpc.polity_id
            AND cc.name = gpc.capital
            and cp.id=%s;
            """
    capitals_info = []
    with connection.cursor() as cursor:
        cursor.execute(query, [pk])
        rows = cursor.fetchall()
    for row in rows:
        cap_dict = {}
        cap_dict['capital'] = row[0]
        cap_dict['latitude'] = row[1]
        cap_dict['longitude'] = row[2]
        capitals_info.append(cap_dict)
    return capitals_info