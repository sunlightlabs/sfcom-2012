"""
Formatting tags and filters.
Currency filter taken from kljensen (http://djangosnippets.org/snippets/552/).
"""
from django import template
import locale

locale.setlocale(locale.LC_ALL, '')

register = template.Library()
  
@register.filter()
def currency(value):
    return locale.currency(value, grouping=True)