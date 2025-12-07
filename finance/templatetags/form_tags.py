from django import template

register = template.Library()


@register.filter
def get_field(form, field_name):
    """Get a form field by name."""
    return form[field_name]


@register.filter
def field_label(bound_field):
    """Get a readable label from field name."""
    label = bound_field.label or bound_field.name
    return label.replace('_', ' ').title()
