from django.urls import path
from django.contrib.auth import views as auth_views
from about import views

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact),
    path('register/', views.regiter, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        next_page=None
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='/'
    ), name='logout'),
    path('sentry-debug/', views.trigger_error),
]

