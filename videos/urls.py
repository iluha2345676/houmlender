from django.urls import path
from .views import feed_view, upload_video_view, like_video_view

urlpatterns = [
    path('feed/',feed_view,name='feed'),
    path('upload/',upload_video_view,name='upload'),
    path('videos/<int:video_id>/like/',like_video_view,name='like_video'),
]