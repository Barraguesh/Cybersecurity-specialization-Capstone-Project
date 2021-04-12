#Python/Django
import datetime
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required

#Models
from messaging.models import Message

#Forms
from messaging.forms import NewMessageForm

@login_required
def index_view(request):
    args = {}
    args["messages"] = Message.objects.all().filter(user_to=request.user.username).order_by('-date')
    return render(request, "index.html", args)

def new_message(request):
    args = {}
    if request.method == 'POST':
        form = NewMessageForm(request.POST)
        if form.is_valid():
            message = Message(user_from=request.user.username, user_to=form.cleaned_data["user_to"], content=form.cleaned_data["message"], date=datetime.datetime.now())
            message.save()
            args["form"] = NewMessageForm()
            args["success"] = True
    else:
        args["form"] = NewMessageForm()
    return render(request, "new_message.html", args)

