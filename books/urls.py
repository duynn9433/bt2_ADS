from django.urls import path

from books import views

urlpatterns = [
    path('', views.index),
    path('author/', views.author_index),
    path('publisher/', views.publisher_index),

    path('<int:id>/change', views.change, name="change"),
    path('author/<int:id>/change', views.change_author),
    path('publisher/<int:id>/change', views.change_publisher),

    path('add/', views.add, name="add"),
    path('author/add/', views.add_author),
    path('publisher/add/', views.add_publisher),

]