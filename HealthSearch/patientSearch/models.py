# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Query(models.Model):
  query_id = models.IntegerField()
  age = models.IntegerField()
  sex = models.BooleanField()
  sympo = models.TextField()
  disease = models.TextField()
  query_last_time = models.DateTimeField
  freq = models.IntegerField()


class DataResource(models.Model):
  resource_id = models.IntegerField()
  resource_name = models.FileField(max_length=15)
  url = models.URLField()
  freq = models.IntegerField()
  published_time = models.DateTimeField()
  descrip = models.TextField()


class ResultURL(models.Model):
  resulturl_id = models.IntegerField()
  shorten_url = models.URLField()
  result_url = models.URLField()
  published_time = models.DateTimeField()
  title = models.TextField()
  freq = models.IntegerField()
  clicks = models.IntegerField()
  last_update_time = models.DateTimeField()


class Query_ResultURL(models.Model):
  query_id = models.ForeignKey(Query, on_delete=models.CASCADE, )
  resultur_id = models.ForeignKey(ResultURL, on_delete=models.CASCADE, )



