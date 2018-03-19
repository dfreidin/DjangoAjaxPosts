# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.
class PostForm(forms.Form):
    add_a_note = forms.CharField(widget=forms.Textarea())