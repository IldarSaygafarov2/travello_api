from django import template
from apps.reports.models import AgentReport


register = template.Library()


@register.simple_tag(takes_context=True)
def get_model_verbose_names(context):
    model = context['model']
    fields = model._meta.get_fields()
    result = []
    for field in fields:
        result.append(field.verbose_name)
    return result

