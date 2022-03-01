from django.urls import path

from . import views

urlspatterns = [
    path('', views.index, {'pagename': ''}, name='home'),
    path('<str:pagename>', views.index, name='index'),
]