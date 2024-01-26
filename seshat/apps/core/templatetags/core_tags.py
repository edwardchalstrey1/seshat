from django import template
from ..views import get_polity_shape_content

register = template.Library()

@register.inclusion_tag('core/polity_map.html')
def polity_map(pk):
    # seshat_id = str(pk)
    seshat_id = "us_united_states_of_america_contemporary"
    content = get_polity_shape_content(seshat_id=seshat_id)

    return {'content': content}
