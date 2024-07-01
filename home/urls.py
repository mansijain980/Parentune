from django.urls import path
from . import views

urlpatterns = [
    path('parents/', views.create_parent),
    path('parents/<int:parent_id>/', views.get_parent),
    path('parents/<int:parent_id>/update/', views.update_parent),
    path('parents/<int:parent_id>/delete/', views.delete_parent),
    path('parents/<int:parent_id>/home-feed/', views.generate_home_feed),
    # Add URLs for CRUD operations for Child and Blog as needed
]
