from django.urls import path, include
from . import views
# from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('about/', views.about_page, name="about_page"),
    path('contact/', views.contact_page, name="contact_page"),

    
]