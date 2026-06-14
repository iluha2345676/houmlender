from django.urls import path
from .views import feed_view, upload_video_view, like_video_view, add_comment_view, video_detail_view, delete_video_view

urlpatterns = [
    path('feed/',feed_view,name='feed'),
    path('upload/',upload_video_view,name='upload'),
    path('videos/<int:video_id>/like/',like_video_view,name='like_video'),
    path('videos/<int:video_id>/comment/',add_comment_view,name='add_comment'),
    path('videos/<int:video_id>/', video_detail_view, name='video_detail'),
    path('videos/<int:video_id>/delete/', delete_video_view, name='delete_video'),
]