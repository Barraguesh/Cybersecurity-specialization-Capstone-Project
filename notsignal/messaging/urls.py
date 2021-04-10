from django.contrib import admin
from django.urls import path

from messaging import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('dbdump', views.dump_db, name='dbdump'),
]