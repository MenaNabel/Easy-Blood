from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class AboutUs(models.Model) :
    #userAcount = models.ForeignKey(User , on_delete='None')
    user = models.CharField(max_length=50)


    title = models.TextField(max_length=50)
    img = models.ImageField(upload_to='AboutUsimgs/' ,  default = 'AboutUsimgs/default.png')
    created = models.DateTimeField(default = timezone.now)
    active = models.BooleanField(default=True)

    def _str_(self):
        return self.title
