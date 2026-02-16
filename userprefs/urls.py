from django.urls import path
from . import views

urlpatterns = [
    path('setpref/', views.set_preference, name='set_preference'),
    path('shows/', views.show_preference, name='show_preference'),
]
