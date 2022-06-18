from django.urls import path, re_path
from . import views
from . import contact

urlpatterns = [
    path('', views.index, name='index'),
    path('add_place/', views.add_place, name='add-place'),
    path('list_subscribers/', views.list_subscriber, name='list-subscribers'),
    path('contact/', contact.contact, name='contact'),
    path('all_todolist/', views.all_todolist, name='show-todolist'),
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/', views.index, name='index'),
]
