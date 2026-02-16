from django.urls import path
from . import views

urlpatterns = [
    path('', views.set_preference, name='set_preference'),
    path('show/', views.show_preference, name='show_preference'),
]
