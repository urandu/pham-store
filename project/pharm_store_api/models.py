from django.db import models

# Create your models here.
class Institution(models.Model):

    INSTITUTION_TYPE = (
        ('hospital',"hospital"),
        ('pharmacy',"pharmacy"),
    )
    name = models.CharField()