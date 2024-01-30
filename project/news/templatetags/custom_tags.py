from datetime import datetime

from django import template


register = template.Library()


@register.simple_tag()
def current_time(format_string='%d %B, %Y'):
    return f'сегодня: {datetime.now().strftime(format_string)}'
