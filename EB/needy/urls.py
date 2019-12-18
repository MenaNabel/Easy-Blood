from django.conf.urls import url
from . import views


app_name = 'needy'

urlpatterns=[
    url(r'^addneedy',views.addNeedy , name='addneedy'),
    url(r'^allneedy',views.allNeedies , name='allneedy')

]
