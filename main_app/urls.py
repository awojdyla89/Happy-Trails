from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('trails/', views.TrailList.as_view(), name='index'),
    path('trails/<int:trail_id>/', views.trails_detail, name='detail'),
    path('trails/create/', views.TrailCreate.as_view(), name='trails_create'),
    path('trails/<int:pk>/update/', views.TrailUpdate.as_view(), name='trails_update'),
    path('trails/<int:pk>/delete/', views.TrailDelete.as_view(), name='trails_delete'),
    path('trails/<int:trail_id>/add_comment/', views.add_comment, name='add_comment'),
    path('accounts/signup/', views.signup, name='signup'),

]