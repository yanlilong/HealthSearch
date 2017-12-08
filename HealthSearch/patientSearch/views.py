# -*- coding: utf-8 -*-



from django.template.loader import get_template
import create_view

from django.http import HttpResponse
from patient_search_form import QueryFrom


def index(request):
  resource_name_list = create_view.create_resource()
  query_form = QueryFrom()
  template = get_template('patientSearch/search_form.html')
  return (HttpResponse(template.render(
      {'query_form': query_form, 'resource_name_list': resource_name_list},
      request)))
