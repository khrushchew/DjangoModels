from django import template

register = template.Library()


@register.filter(name='word_filter')
def currency(value):
   words = ['редиску', 'какашка', 'дурак', 'идиот']

   for i in words:
      if i in value:
         value = value.replace(i, '*' * len(i))
   return value


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   for k, v in kwargs.items():
       d[k] = v
   return d.urlencode()