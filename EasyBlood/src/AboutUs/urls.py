from django.conf.urls import url
from . import views


app_name = 'AboutUs'
urlpatterns = {
    url(r'^$',views.all_posts, name='all_posts'),
    url(r'^(?P<id>\d+)$' , views.post , name='post'),
    url(r'^create$',views.create_post, name='create_post'),
    url(r'^(?P<id>\d+)/edit$' , views.edit_post , name='edit_post'),
}
