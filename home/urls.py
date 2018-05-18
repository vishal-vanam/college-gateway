from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
path('adduser/', views.adduser, name='adduser'),
    path('search/', views.search, name='search'),
   path('signin/', views.signin, name='signin'),
   path('display/', views.display, name='display'),
   path('users/', views.users, name='users'),
   path('user/', views.user, name='user'),
   path('user/profile', views.profile, name='profile'),

    url(r'^(?P<college_id>[0-9]+)/$', views.details, name='Details'),
    url(r'^user/predictor/$', views.predictor, name='predictor'),
	url(r'^check/$', views.check, name='check'),

]
