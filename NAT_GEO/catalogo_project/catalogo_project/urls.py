"""
URL configuration for catalogo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from catalogo import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.verIndexHome, name ='index'),
    path('<int:id>/', views.pelicula_detail, name='pelicula-detail'),
    path('register/', views.register, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('catalogo/', views.catalog_view, name='catalog_view'),
    path('chat/', views.chat_view, name='chat'),
    path('api/', include('catalogo.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
