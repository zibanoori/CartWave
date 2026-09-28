from django.db import models

class product(models.model):
    name = models.CharField(max_length=200)