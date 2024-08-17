# home/urls.py
from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),  # Home page
    path('receipes', views.receipes, name='receipes'),  # Home page
    path('update_reciepe/', views.update_reciepe, name='update_reciepe'),  # About page
    path('delete_reciepe/', views.delete_reciepe, name='delete_reciepe'),  # Contact page
  

]
