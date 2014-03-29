from django import forms
from django.utils import formats
from django.core.exceptions import ValidationError
from widgets import Html5TextInput, Html5PasswordInput, Html5CheckboxInput
from widgets import Html5SearchInput, Html5EmailInput
from widgets import Html5URLInput, Html5NumberInput, Html5RangeInput
from django.core import validators, exceptions
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy as _
import urlparse

__all__ = (
        'Html5Field', 'Html5CharField', 'Html5PasswordField',
        'Html5SearchField', 'Html5EmailField', 'Html5URLField',
        'Html5IntegerField', 'Html5BooleanField', 'Html5RangeField',
        )
  
  
class Html5Field(forms.fields.Field):
    """Base class for Html5 Fields
  
    Used only for extending
  
    :param placeholder: placeholder text to display if field in unfocused
    :type placeholder: String
    :param autofocus: should the field be focused on load
    :type autofocus: Boolean
    """
  
    def __init__(self, choices=(), placeholder=None, autofocus=False, class_attr=[],
            *args, **kwargs):
        self.placeholder = placeholder
        self.autofocus = autofocus
        self.class_attr = class_attr
        self.choices = choices
        super(Html5Field, self).__init__(*args, **kwargs)
  
  
    def widget_attrs(self, widget):
        widget_attrs = super(Html5Field, self).widget_attrs(widget)
        current_class = widget_attrs.get('class', '').split()
  
        if self.placeholder:
            widget_attrs['placeholder'] = self.placeholder
  
        if self.autofocus:
            widget_attrs['autofocus'] = None
  
        if self.required:
            widget_attrs['required'] = None
            current_class.append('required')
  
        if isinstance(self.class_attr, (str, unicode)):
            self.class_attr = self.class_attr.split()    
  
        for classitem in self.class_attr:
            if classitem not in current_class:
                current_class.append(classitem)
  
        if current_class:
            widget_attrs['class'] = ' '.join(current_class)
  
        return widget_attrs
  
  
class Html5BooleanField(Html5Field):
    widget = Html5CheckboxInput
  
    def to_python(self, value):
        """Returns a Python boolean object."""
        # Explicitly check for the string 'False', which is what a hidden field
        # will submit for False. Also check for '0', since this is what
        # RadioSelect will provide. Because bool("True") == bool('1') == True,
        # we don't need to handle that explicitly.
        if value in ('False', '0'):
            value = False
        else:
            value = bool(value)
        value = super(Html5BooleanField, self).to_python(value)
        if not value and self.required:
            raise ValidationError(self.error_messages['required'])
        return value
  
    def widget_attrs(self, widget):
        widget_attrs = {}
  
        if self.autofocus:
            widget_attrs['autofocus'] = None
  
        if self.required:
            widget_attrs['required'] = None
  
        return widget_attrs