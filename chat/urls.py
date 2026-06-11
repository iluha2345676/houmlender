from django.urls import path
from .views import chat_detail_view

urlpatterns = [
    path('chat/<int:user_id>', chat_detail_view, name='chat_detail'),
]