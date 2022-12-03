from django.urls import path
from . import views
from .views import *

urlpatterns =[
    path('',views.homepage, name='home' ),
    path('about/', views.aboutpage, name='about'),
    path('property/', Property.as_view(),name='property'),
    path('createproperty/', views.createproperty,name='createproperty'),
    path('property1',views.property1, name='property1'),
    path('contact/', views.contactpage, name='contact'),
    #path('registration/login', views.login, name='login'),

]