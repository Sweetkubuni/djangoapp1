# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=50)
    post_text  = models.CharField(max_length=400)
    post_date  = models.DateField()

    def __str__(self):
        return self.post_title