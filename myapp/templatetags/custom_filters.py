from django import template

register = template.Library()

@register.filter
def lookup(dictionary, key):
    return dictionary.get(key)

from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

# myapp/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
