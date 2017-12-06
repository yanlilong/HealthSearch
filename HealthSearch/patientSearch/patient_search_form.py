from django.forms import ModelForm, Textarea, Select
from django import forms
from models import Query, DataResource
from django.utils.translation import ugettext as _


class QueryFrom(ModelForm):
  class Meta:
    model = Query
    labels = {
      'age': "Age",
      'sex': "Gender",
      'sympo': 'Sympotom',
      'disease': 'Disease'
    }
    fields = ('age', 'sex', 'sympo', 'disease')

    SEX_CHOICES = (
      ('True', 'Female'),
      ('False', 'Male'),
    )

    widgets = {
      'sex': Select(attrs={'class': 'select'}, choices=SEX_CHOICES),
      'sympo': Textarea(attrs={'cols': 30, 'rows': 2}),
      'disease': Textarea(attrs={'cols': 30, 'rows': 2}),
    }
