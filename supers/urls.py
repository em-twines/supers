from django.urls import path
from . import views


urlpatterns = [
    path('', views.supers),
    path('<int:pk>/', views.super_details)


]