from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class donar(models.Model) :
    user = models.CharField(User , on_delete='CASCADE')
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=250)
    bloodType = models.CharField(max_length=3)
    dateOfLastDanation = models.DateField()
    age = models.IntegerField()
    weight = models.IntegerField()
    city = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)

    def _str_(self):
        return self.title
