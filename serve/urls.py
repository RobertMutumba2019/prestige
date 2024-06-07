from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/', views.gallery, name='gallery'),
   
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('home/', views.home, name='home'),
    path('services/', views.services, name='services'),
     path('book/<int:car_id>/', views.book, name='book'),
    path('book/<int:car_id>/', views.book, name='book_car'),


]