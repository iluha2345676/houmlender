from django.db.models import Model
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import VideoForm, CommentForm
from .models import Video, Like


def feed_view(request):
    videos = Video.objects.all().order_by('-created_at')

    return render(request,'videos/feed.html',{'videos':videos})

@login_required
def upload_video_view(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)

        if form.is_valid():
            video = form.save(commit=False)
            video.author = request.user
            video.save()

            return redirect('feed')

        else:
            print(form.errors)

    else:
        form = VideoForm()

    return render(request,'videos/upload_video.html',{'form':form})

@login_required
def like_video_view(request,video_id):
    video = get_object_or_404(Video, id=video_id)

    like = Like.objects.filter(user=request.user, video=video).first()

    if like:
        like.delete()
    else:
        Like.objects.create(user=request.user, video=video)


    return redirect('feed')

@login_required
def add_comment_view(request,video_id):
    video = get_object_or_404(Video, id=video_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.video = video

            comment.save()

    return redirect('feed')

def video_detail_view(request,video_id):
    video = get_object_or_404(Video, id=video_id)

    return render(request,'videos/video_detail.html',{'video':video})

@login_required
def delete_video_view(request,video_id):
    video = get_object_or_404(Video, id=video_id)

    if video.author != request.user:
        return redirect('feed')

    if request.method == 'POST':
        video.delete()
        return redirect('feed')

    return redirect('video_detail',video_id=video_id)