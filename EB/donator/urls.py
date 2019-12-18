from django.conf.urls import url
from . import views


app_name = 'donator'

urlpatterns=[
    url(r'^adddonator',views.addDonator , name='adddonator')
]
