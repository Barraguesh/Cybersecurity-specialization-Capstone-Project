from django.contrib import admin
from django.urls import path

from messaging import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('new_message', views.new_message, name='new_message'),
    #Extra
    path('dbdump', views.dump_db, name='dbdump'),
]