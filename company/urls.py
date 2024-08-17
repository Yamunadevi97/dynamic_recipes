"""
URL configuration for company project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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


"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from home import views
from home.views import *
from dishes.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    #path('',home,name="home"),
    path('',receipes,name="receipes"),
    path('receipes/',receipes,name="receipes"),
    path('delete-reciepe/<id>/',delete_reciepe,name="delete_reciepe"),
    path('update-reciepe/<id>/',update_reciepe,name="update_reciepe"),
     path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('piz/', views.pizza, name='pizza'),
    path('bur/', views.burger, name='burger'),
    path('no/', views.noodles, name='noodles'),
    path('sand/', views.sandwich, name='sandwich'),
     path('grav/', views.gravy, name='gravy'),
     path('soup/', views.soup, name='soup'),
    # other URL patterns
    path('home/', views.home, name='home'),
    # other URL patterns
     path('new/', views.new, name='new'),
    path('login/',login_page,name="login_page"),
    path('register/',register,name="register"),
    path('logout/',logout,name="logout"),
   path('success_page/',success_page,name="success_page"),
   
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns+=staticfiles_urlpatterns()