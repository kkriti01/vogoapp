from __future__ import unicode_literals

from django.db import models


class Cake(models.Model):
    name = models.CharField(max_length=225)
    price = models.CharField(max_length=225)
    image = models.CharField(max_length=225)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=225)
    cake = models.ManyToManyField(Cake)

    def __unicode__(self):
        return self.name
