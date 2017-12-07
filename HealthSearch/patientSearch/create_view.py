from models import DataResource


def create_resource():
  resource_name_list = []
  for data_resource in DataResource.objects.all():
    resource_name_list.append(data_resource.resource_name)
    print(resource_name_list)
  return resource_name_list


'''
p = DataResource(resource_name='webmed',
                 url='https://www.webmd.com/heart-disease/heart-failure/default.htm',
                 freq=0,
                 descrip='ebMD has created an organization that we believe fulfills the promise of health information on the Internet. We provide credible information, supportive communities, and in-depth reference material about health subjects that matter to you.')
DataResource(resource_name='tripdatabase',
             url='https://www.tripdatabase.com/search?criteria=headache&lang=en',
             freq=0,
             descrip='Trip is a clinical search engine designed to allow users to quickly and easily find and use high-quality research evidence to support their practice and/or care.')
'''
