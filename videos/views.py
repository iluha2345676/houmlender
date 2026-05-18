from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import VideoForm
from .models import Video, Like


def feed_view(request):
    videos = Video.objects.all().order_by('-created_at')

    return render(request,'videos.html',{'videos':videos})

@login_required
def upload_video_view(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)

        if form.is_valid():
            video = form.save(commit=False)
            video.author = request.user
            video.save()

            return redirect('/videos/')

    else:
        form = VideoForm()

    return render(request,'videos.html',{'form':form})

@login_required
def like_video_view(request):
    video = get_object_or_404(Video, id=request.POST.get('video_id'))

    like = Like.objects.filter(user=request.user, video=video).first()

    if like:
        like.delete()
    else:
        Like.objects.create(user=request.user, video=video)


    return redirect('feed')
