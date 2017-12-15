from patientSearch.models import Query, DataResource
from django.core.exceptions import ObjectDoesNotExist
import logging

logger = logging.getLogger('patientSearch/datasource_service')


def dataresource_is_exsit(name):
  if (DataResource.objects.filter(resource_name=name).exists()):
    return True
  else:
    logger.warning(
        msg='Dataresource with resource name %s dose not exist.' % name)
    return False


def get_dataresource(name):
  try:
    dataresource = DataResource.objects.get(resource_name=name)
    logger.info(msg=dataresource.url)
    return dataresource.url
  except ObjectDoesNotExist:
    logger.error(msg='selected Dataresource dose not exist')
    # return a default url
    return None


def create_resource():
  resource_name_list = []
  for data_resource in DataResource.objects.all():
    resource_name_list.append(data_resource.resource_name)
  return resource_name_list
