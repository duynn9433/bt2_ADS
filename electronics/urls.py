from django.urls import path

from electronics import views

urlpatterns = [
    path('', views.index),
    path('size/', views.size_index),

    path('<int:id>/change', views.change),
    path('size/<int:id>/change', views.size_change),

    path('add/', views.add),
    path('size/add/', views.add_size),

]