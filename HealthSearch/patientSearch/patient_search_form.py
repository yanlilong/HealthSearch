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
      'age': Textarea(attrs={'cols': 4, 'rows': 1}),
      'sex': Select(attrs={'class': 'select'}, choices=SEX_CHOICES),
      'sympo': Textarea(attrs={'cols': 50, 'rows': 1}),
      'disease': Textarea(attrs={'cols': 50, 'rows': 1}),
    }
