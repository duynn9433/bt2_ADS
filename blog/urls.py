from django.urls import path

from blog import views

urlpatterns=[
    path('', views.list),
    path('<int:id>/', views.post)
]