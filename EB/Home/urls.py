from django.conf.urls import url
from . import views
from needy import views as v


app_name = 'Home'

urlpatterns=[
    url(r'^$',views.index , name='index') ,
    url(r'^$',v.allNeedies , name='allneedies')

]
