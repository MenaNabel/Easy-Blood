from django.conf.urls import url
from . import views


app_name = 'donator'

urlpatterns=[
    url(r'^addDonator',views.addDonator , name='addDonator')
]
