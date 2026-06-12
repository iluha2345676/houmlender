from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from .forms import MessageForm
from .models import Message

@login_required
def chat_detail_view(request,user_id):
    other_user = get_object_or_404(User,id=user_id)


    message = Message.objects.filter(Q(sender=request.user, recipient=other_user) | Q(sender=other_user,recipient=request.user))

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = other_user
            message.save()

            return redirect('chat_detail',user_id=other_user.id)

        else:
            form = MessageForm()
    return render(request,'chat/chat_detail.html',{'form':form,'message':message,'other_user':other_user})