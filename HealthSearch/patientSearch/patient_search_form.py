from django.forms import ModelForm, Textarea, Select
from django import forms
from models import Query, DataResource
from django.utils.translation import ugettext_lazy as _


class QueryFrom(ModelForm):
  class Meta:
    model = Query
    fields = ('age', 'sex', 'sympo', 'disease',)
    SEX_CHOICES = ((True, 'Female'),
                   (False, 'Male'))
    widgets = {
      'sex': Select(attrs={'class': 'select',
                           'choices': SEX_CHOICES,
                           'initial': 'Female',
                           'cols':3,
                           'rows':3}),
      'sympo': Textarea(attrs={'cols': 30, 'rows': 2}),
      'disease': Textarea(attrs={'cols': 30, 'rows': 2}),
    }
    labels = {
      'age': _('Age'),
      'sex': _('Gender'),
      'sympo': _('Sympotom'),
      'disease': _('Disease'),
    }
