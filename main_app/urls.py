from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('trails/', views.TrailList.as_view(), name='index'),
    path('trails/<int:pk>/', views.TrailDetail.as_view(), name='detail'),
    path('trails/create/', views.TrailCreate.as_view(), name='trails_create'),

]