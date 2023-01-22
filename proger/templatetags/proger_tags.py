from django import template
from proger.models import Category


register = template.Library()

@register.simple_tag(name="getcats")
def get_categories():
    return Category.objects.all()