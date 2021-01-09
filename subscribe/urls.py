from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_subscribe, name='user_subscribe'),
]