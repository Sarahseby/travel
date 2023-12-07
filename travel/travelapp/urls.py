from . import views
from django.urls import path

urlpatterns = [

    #path('',views.demo,name='demo'),
    path('', views.tem, name='tem'),
  #  path('add/',views.addition,name="addition"),
]
