# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string 


# Create your views here.

def index(request):
    request.session['count'] += 1
    ranword = get_random_string(length=14, allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    request.session['word'] = ranword
    return render( request, 'rword/index.html', {'ranword': ranword} )

def generate(request):
    return redirect('/')

def reset(request):
    request.session['count'] = 0
    ranword = request.session['word']
    return render(request, 'rword/index.html', {'ranword': ranword} )