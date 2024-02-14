# custom_tags.py

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def include_image(image):
    tag = f'<img class="size-9 rounded-full" src="{image}" alt="user photo">'
    return mark_safe(tag)
