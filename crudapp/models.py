# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Inventory(models.Model):
    item_id = models.IntegerField(default=0)
    item_name = models.CharField(max_length=200)
    brand_name = models.CharField(max_length=200)
    item_available_qty = models.IntegerField(default=0)
    last_updated = models.DateTimeField('updated date')

    def __str__(self):
        return str(self.item_id) + ' ' + str(self.id)

