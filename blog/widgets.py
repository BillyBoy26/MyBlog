from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from django import forms


# https://concentricsky.com/articles/detail/custom-django-widget
class RichText(forms.widgets.Textarea):
    template_name = 'blog/widgets/rich_text.html'

    def render(self, name, value, attrs=None):
        text_area_html = super(RichText, self).render(name, value, attrs)
        context = {
            'textAreaHtml': text_area_html
        }
        return mark_safe(render_to_string(self.template_name, context))
