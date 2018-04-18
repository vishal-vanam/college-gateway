from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('signup/', views.UserFormView, name='signup'),
   path('signin/', views.signin, name='signin'),
   path('display/', views.display, name='display'),
   path('users/', views.users, name='users'),
   path('user/', views.user, name='user'),
   path('user/profile', views.profile, name='profile'),

    url(r'^(?P<college_id>[0-9]+)/$', views.details, name='Details'),
    url(r'^users/(?P<user_id>[0-9]+)/$', views.predictor, name='Predictor'),
	url(r'^check/$', views.detail7, name='detail7'),

]
