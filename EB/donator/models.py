from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class donator(models.Model) :
    user = models.ForeignKey(User , on_delete='None')
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=250)
    bloodType = models.CharField(max_length=3)
    #dateOfLastDanation = models.DateField(default= timezone.datetime)
    age = models.IntegerField()
    weight = models.IntegerField()
    city = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.firstName
