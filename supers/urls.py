from django.urls import path
from . import views


urlpatterns = [
    # path('', views.supers),
    path('', views.display_chosen_type),
    path('<int:pk>/', views.super_details)


]