# -*- coding: utf-8 -*-



from django.template.loader import get_template

from django.http import HttpResponse
from patient_search_form import QueryFrom
from django.shortcuts import render

webmed = "web"


def index(request):
  query_form = QueryFrom()
  template = get_template('patientSearch/search_form.html')
  return (HttpResponse(template.render({'query_form':query_form},request)))
