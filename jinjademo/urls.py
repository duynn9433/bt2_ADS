from django.urls import path

from jinjademo import views
from django.views.generic import TemplateView
urlpatterns = [
    path('', views.index),
    path('detail', views.detail),
    path('macro',views.macro),
]