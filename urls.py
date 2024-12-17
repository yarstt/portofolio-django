from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_umum, name='profile_umum'),
    path('pendidikan/', views.profile_pendidikan, name='profile_pendidikan'),
    path('pengalaman/', views.profile_pengalaman, name='profile_pengalaman'),
    path('sosmed/', views.profile_sosmed, name='profile_sosmed'),
]
