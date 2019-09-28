from django.db import models

# Create your models here.
class Institution(models.Model):

    INSTITUTION_TYPE = (
        ('hospital',"hospital"),
        ('pharmacy',"pharmacy"),
    )
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100, choices=INSTITUTION_TYPE)
    contact_person = models.CharField(max_length=100)