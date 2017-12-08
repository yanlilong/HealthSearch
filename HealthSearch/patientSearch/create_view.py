from models import DataResource


def create_resource():
  resource_name_list = []
  for data_resource in DataResource.objects.all():
    resource_name_list.append(data_resource.resource_name)
    print(resource_name_list)
  return resource_name_list
