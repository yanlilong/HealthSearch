# -*- coding: utf-8 -*-



from django.template.loader import get_template

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from patientSearch.patient_search_form import QueryFrom
from patientSearch.service import query_service
from patientSearch.service import dataresource_service

import logging

logger = logging.getLogger("patientSearch")


def index(request):
  template = get_template('patientSearch/search_form.html')
  error_400 = get_template('patientSearch/400.html')
  resource_name_list = dataresource_service.create_resource()
  if (request.method == 'POST'):
    query_form = QueryFrom(request.POST)
    print(query_form.fields)
    if (query_form.is_valid()):
      age = request.POST.get("age", "")
      sex = request.POST.get("sex", "")
      sympo = request.POST.get("sympo", "")
      disease = request.POST.get("disease", "")

      query_service.save_query(age, sex, sympo, disease)
      selected_datsource = request.POST.get("datasource_list", "")

      if (dataresource_service.dataresource_is_exsit(selected_datsource)):
        resource_name_list.remove(selected_datsource)
        resource_name_list.insert(0, selected_datsource)
        url = dataresource_service.get_dataresource(selected_datsource)
        print(url)
        logger.info(msg=url)
      else:
        return (HttpResponse(error_400.render(request)))
        # rest_url = url?age=)age&sex=create_view.create_sex(sex)&sym
        # return redirect('/patientSearch')
    return (HttpResponse(template.render(
        {'query_form': query_form, 'resource_name_list': resource_name_list},
        request)))

  else:

    query_form = QueryFrom()
    template = get_template('patientSearch/search_form.html')
    return (HttpResponse(template.render(
        {'query_form': query_form, 'resource_name_list': resource_name_list},
        request)))
