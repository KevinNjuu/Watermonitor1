# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Network(models.Model):
    network_name = models.CharField(max_length=200)
    network_code = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    mobile = models.IntegerField(default= 0)
    physical_address = models.TextField()

    def __str__(self):
        return self.network_name

class Primary_canal(models.Model):
    primary_canal_name = models.CharField(max_length=200)
    primary_canal_code = models.CharField(max_length=100)
    network = models.ForeignKey(Network, on_delete=models.CASCADE)

    def __str__(self):
        return self.primary_canal_name

class Secondary_canal(models.Model):
    secondary_canal_name = models.CharField(max_length=200)
    secondary_canal_code = models.CharField(max_length=100)
    primary_canal = models.ForeignKey(Primary_canal, on_delete=models.CASCADE)

    def __str__(self):
        return self.secondary_canal_name


class Tertiary_canal(models.Model):
    tertiary_canal_name = models.CharField(max_length=200)
    tertiary_canal_code = models.CharField(max_length=100)
    secondary_canal = models.ForeignKey(Secondary_canal, on_delete=models.CASCADE)

    def __str__(self):
        return self.tertiary_canal_name