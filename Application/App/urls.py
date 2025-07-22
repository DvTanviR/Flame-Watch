from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('predict/', views.WildfirePredictionAPI.as_view(), name='wildfire-predict'),

]
