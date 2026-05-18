import profile

from django.urls import path, include
from .views import registration_view, login_view, logout_view,profile_view

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),

]