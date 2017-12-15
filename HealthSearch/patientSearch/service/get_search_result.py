QUERY_STRING = '?query='


def get_search_url(data_resource_url, age, sypom, disease):
  search_url = data_resource_url + QUERY_STRING + get_search_param(age=age,
                                                                   sypom=sypom,
                                                                   disease=disease)
  return search_url


def get_search_param(age, sypom, disease):
  param = get_age_domain(age=age) + '+' + sypom + '+' + disease

  return param


def get_age_domain(age):
  if ((age > 0) & (age <= 16)):
    search_age = 'child'
  elif ((age > 16) & (age <= 44)):
    search_age = 'youth'
  elif ((age > 44) & (age <= 59)):
    search_age = 'middle age'
  elif (age > 59):
    search_age = 'old age'
  return search_age

