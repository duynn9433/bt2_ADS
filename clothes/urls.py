from django.urls import path

from clothes import views

urlpatterns = [
    path('', views.index),
    path('vendor/', views.vendor_index),

    path('<int:id>/change', views.change),
    path('vendor/<int:id>/change', views.vendor_change),

    path('add/', views.add),
    path('vendor/add/', views.add_vendor),

]