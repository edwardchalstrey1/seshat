from django import template
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
    return {'content': content}
