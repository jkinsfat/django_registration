# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from secret_page.models import User
# Create your views here.
def index(request):
    context = {}
    if 'context' in request.session:
        context = request.session['context']
        request.session.pop('context')
    return render(request, 'secret_page/login.html', context)

def secrets(request):
    return render(request, 'secret_page/index.html')

def popular(request):
    return render(request, 'secret_page/popular.html')

def login(request):
    try:
        useraccount = User.objects.filter(email=request.POST['login_email'])[0]
        if useraccount.password == request.POST['login_password']:
            return redirect('/secrets')
    except:
        request.session['context'] = {'login_error' : 'One of these fields is incorrect'}
    return redirect('/')

def register(request):
    context = {}
    if request.POST['password'] != request.POST['password_confirm']:
        context['password_confirm'] = 'Does not match password'
    new_user = User(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=request.POST["password"])
    try:
        new_user.full_clean()
    except ValidationError as e:
        for key in e:
            context[key[0]] = key[1][0]
    if context == {}:
        new_user.save()
        context['result'] = 'Registration complete! Try logging in'
    else:
        context['result'] = 'Registration incomplete, correct errors above'
    request.session['context'] = context
    return redirect('/')

def process(request, datatype):
    return redirect('/secrets')
