from patientSearch.models import Query
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
import logging

logger = logging.getLogger('patientSearch/query_service')


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


def create_sex(sex):
  if (sex == True):
    return "Female"
  elif (sex == False):
    return "Male"
