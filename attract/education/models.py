from __future__ import unicode_literals
from django.db import models


class People(models.Model):
    """ Collect person names """
    person_name = models.CharField(max_length=120)

    def __unicode__(self):
        return self.person_name


class Document(models.Model):
    """ Keeps information about education """
    person_education = models.CharField(max_length=120)
    person_id = models.ForeignKey(People, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.person_education
