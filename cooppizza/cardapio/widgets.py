from django import forms
from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode
from util import flatatt, render_datalist
from django.utils.html import conditional_escape

class Html5CheckboxInput(forms.widgets.CheckboxInput):
    input_type = 'checkbox'
  
    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs, type='checkbox', name=name)
        try:
            result = self.check_test(value)
        except: # Silently catch exceptions
            result = False
        if result:
            final_attrs['checked'] = 'checked'
        if value not in ('', True, False, None):
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_unicode(value)
        return mark_safe(u'<input%s />' % flatatt(final_attrs))