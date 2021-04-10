#Python/Django
import datetime
import os
import sqlite3
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required

#Models
from messaging.models import Message

@login_required
def index_view(request):
    args = {}
    return render(request, 'index.html', args)

def dump_db(request):
    args = {}
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT * FROM messaging_message")
    messages = c.fetchall()
    c.execute("SELECT * FROM auth_user")
    user_data = c.fetchall()
    output = open(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/notsignal/templates/dump_db.html",'w')
    output.write("<h1>DB dump</h1>")
    output.write(str(f"{user_data}<hr>"))
    output.write(str(messages))
    output.close()
    return render(request, 'dump_db.html', args)
