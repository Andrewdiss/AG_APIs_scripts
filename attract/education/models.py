from __future__ import unicode_literals
from django.db import models


class Person(models.Model):
    person_name = models.CharField(max_length=120)

    def __unicode__(self):
        return self.person_name


class Document(models.Model):
    person_education = models.CharField(max_length=120)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.person_education
