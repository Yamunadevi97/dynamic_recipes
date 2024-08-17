# home/urls.py
from django.urls import path
from home import views

urlpatterns = [
    path('home/', views.home, name='home'), 
    path('about/', views.about, name='about'),  # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('success/', views.success_page, name='success_page'),  # Success page
  

]
