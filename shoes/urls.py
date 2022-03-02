from django.urls import path

from shoes import views

urlpatterns = [
    path('', views.index),
    path('brand/', views.brand_index),

    path('<int:id>/change', views.change),
    path('brand/<int:id>/change', views.brand_change),

    path('add/', views.add),
    path('brand/add/', views.add_brand),

]