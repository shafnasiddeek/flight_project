from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('add/', views.add_route_view, name='add_route'),
    path('nth-node/', views.nth_node_view, name='nth_node'),
    path('longest/', views.longest_route_view, name='longest_route'),
    path('shortest/', views.shortest_path_view, name='shortest_path'),
]
