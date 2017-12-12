from models import Query, DataResource
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
import pdb
import logging
logger = logging.getLogger('patientSearch')


def save_query(age, sex, sympo, disease):
  try:
    query = Query.objects.get(age=age, sex=sex, sympo=sympo, disease=disease)
    query.freq = query.freq + 1
    query.query_last_time = timezone.now()
  except ObjectDoesNotExist:
    logger.info(msg="a new Queryparameter will be saved in database")
    query = Query(age=age, sex=sex, sympo=sympo, disease=disease,
                  query_last_time=timezone.now(), freq=0)

  query.save()


def get_dataresource(name):
  try:
    dataresource = DataResource.objects.get(resource_name=name)
    logger.info(msg=dataresource.url)
    return dataresource.url
  except ObjectDoesNotExist:
    logger.error(msg="selected Dataresource is not exist")
    # return a default url
    return None


def create_resource():
  resource_name_list = []
  for data_resource in DataResource.objects.all():
    resource_name_list.append(data_resource.resource_name)
  return resource_name_list


def create_sex(sex):
  if (sex == True):
    return "Female"
  elif (sex == False):
    return "Male"
