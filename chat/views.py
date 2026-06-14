from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from .forms import MessageForm
from .models import Message

@login_required
def chat_detail_view(request,user_id):
    other_user = get_object_or_404(User,id=user_id)


    messages = Message.objects.filter(Q(sender=request.user, recipient=other_user) | Q(sender=other_user,recipient=request.user)).order_by('created_at')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            messages = form.save(commit=False)
            messages.sender = request.user
            messages.recipient = other_user
            messages.save()

            return redirect('chat_detail',user_id=other_user.id)

    else:
        form = MessageForm()
    return render(request,'chat/chat_detail.html',{'form':form,'messages':messages,'other_user':other_user})