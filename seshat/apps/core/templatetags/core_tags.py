from django import template
from ..models import Polity
from ..views import get_polity_shape_content

register = template.Library()

@register.inclusion_tag('core/polity_map.html')
def polity_map(pk):
    page_id = str(pk)
    seshat_id = get_seshat_id_from_page_id(page_id)
    content = get_polity_shape_content(seshat_id=seshat_id)
    return {'content': content}


def get_seshat_id_from_page_id(page_id):
    polity = Polity.objects.get(id=page_id)
    return polity.new_name