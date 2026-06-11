

from django.urls import path, include
from .views import registration_view, login_view, logout_view, user_profile_view, follow_view

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path("users/<int:user_id>/", user_profile_view, name="user_profile"),
    path("users/<int:user_id>/follow/", follow_view, name="follow"),
]