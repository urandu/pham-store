from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Institution(models.Model):

    INSTITUTION_TYPE = (
        ('hospital',"hospital"),
        ('pharmacy',"pharmacy"),
    )
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100, choices=INSTITUTION_TYPE)
    contact_person = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

