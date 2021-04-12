#Python/Django
import sqlite3
import os
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from pathlib import Path
from django.contrib.auth.models import User

#Messaging
from messaging.views import index_view

def registration_view(request):
    args = {}
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(username=form.cleaned_data['username'], email=request.POST['email'], password=form.cleaned_data['password1'])
            return index_view(request)
        else:
            args["form"] = UserCreationForm(request.POST)
    else:
        args["form"] = UserCreationForm()
    return render(request,'registration/signup.html', args)

def check_email_view(request):
    args = {}
    emails_folder = Path(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/sent_emails").rglob("*.log")
    args["content"] = ""
    for email in emails_folder:
        f = open(email, 'r')  
        args["content"] = f"{args['content']}<br>{f.readlines()}"
        f.close()
    return render(request,'email.html', args)

def dump_db(request):
    args = {}
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    c.execute("SELECT * FROM messaging_message")
    messages = c.fetchall()
    c.execute("SELECT * FROM auth_user")
    user_data = c.fetchall()
    output = open(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/notsignal/templates/dump_db.html","w")
    output.write("<h1>DB dump</h1>")
    output.write(str(f"{user_data}<hr>"))
    output.write(str(messages))
    output.close()
    return render(request, "dump_db.html", args)
