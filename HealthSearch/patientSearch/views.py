# -*- coding: utf-8 -*-


from django.template import RequestContext
from django.template.loader import get_template
from django.http import HttpResponse


def index(request):
  template = get_template('patientSearch/search_form.html')
  return HttpResponse.get(template.render({'name': 'world'}, request))
