"""bt2_ADS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
import jinjademo.views
from about import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base_bt2.html')),
    # path('about/', views.contact),
    # re_path(r'^about/', TemplateView.as_view(template_name='about/contact.html')),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('jinjademo/', include('jinjademo.urls')),
    path('about/', include('about.urls')),

    path('book/', include('books.urls')),
    path('mobile/', include('mobile_phones.urls')),
    path('cloth/', include('clothes.urls')),
    path('shoe/', include('shoes.urls')),
    path('electronic/', include('electronics.urls')),
    path('laptop/', include('laptops.urls')),
    path('blog/', include('blog.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

