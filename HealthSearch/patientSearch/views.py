# -*- coding: utf-8 -*-



from django.template.loader import get_template

from django.http import HttpResponse
from django.shortcuts import render

webmed = "web"


def index(request):
   template = get_template('patientSearch/search_form.html')
   return (HttpResponse(template.render({'webmed': webmed}, request)))
 # context = {'webmed': webmed}
  #return render(request, 'patientSearch/search_form.html')
