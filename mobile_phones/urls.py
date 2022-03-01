from django.urls import path

from mobile_phones import views

urlpatterns = [
    path('', views.index),
    path('memory/', views.memory_index),
    path('producer/', views.producer_index),

]
