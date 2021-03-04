from django.urls import path
from . import views

urlpatterns = [
    path('',views.locationView, name='locationview'),
]
