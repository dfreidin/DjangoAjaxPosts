# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.html import escape
from .models import *

# Create your views here.
def index(request):
    if not "posts" in request.session:
        request.session["posts"] = []
    form = PostForm()
    return render(request, "posts/index.html", {"form": form})

def add_post(request):
    if request.method != "POST":
        return redirect(index)
    if not "posts" in request.session:
        request.session["posts"] = []
    form = PostForm(request.POST)
    if form.is_valid():
        post_text = escape(form.cleaned_data["add_a_note"])
        request.session["posts"].append(post_text)
        request.session.modified = True
        return render(request, "posts/new_post.html", {"post_text": post_text})
    return HttpResponse("")