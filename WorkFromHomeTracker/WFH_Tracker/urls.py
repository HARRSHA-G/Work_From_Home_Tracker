from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),  # Home page
    path('submit/', views.submit_form, name='submit_form'),  # Form submission
]
