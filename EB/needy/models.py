from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.

class needy(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    hospital = models.CharField(max_length=50)
    blood_Type = models.CharField(max_length=3)
    age = models.IntegerField()
    donation_type = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    created = models.DateTimeField(default=timezone.now)
    desciption = RichTextField()


    def __str__(self):
        return self.name