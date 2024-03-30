from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name='app'),
    path('refraiche/', views.refraiche, name='refraiche'),
    path('enregistement/', views.enregistement, name='enregistement'),
]
