from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('words', views.words, name='words'),
    path('list-users', views.ListUsers.as_view(), name='list-users'),
    path('test_get_post', views.test_get_post, name='test_get_post'),

]
