# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Query(models.Model):
  age = models.IntegerField()
  sex = models.BooleanField()
  sympo = models.TextField()
  disease = models.TextField()
  query_last_time = models.DateTimeField
  freq = models.IntegerField()


class DataResource(models.Model):
  resource_name = models.FileField(max_length=15)
  url = models.URLField()
  freq = models.IntegerField()
  published_time = models.DateTimeField()
  descrip = models.TextField()


class ResultURL(models.Model):
  shorten_url = models.URLField()
  result_url = models.URLField()
  published_time = models.DateTimeField()
  title = models.TextField()
  freq = models.IntegerField()
  clicks = models.IntegerField()
  last_update_time = models.DateTimeField()


class Query_ResultURL(models.Model):
  query = models.ForeignKey(Query, on_delete=models.CASCADE)
  result_url = models.ForeignKey(ResultURL, on_delete=models.CASCADE)


class ResultURL_DataResource(models.Model):
  result_url=models.ForeignKey(ResultURL, on_delete=models.CASCADE)
  data_resource=models.ForeignKey(DataResource,on_delete=models.CASCADE)
