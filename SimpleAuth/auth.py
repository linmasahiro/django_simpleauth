# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.contrib import auth


def index(request):
    """登入畫面
    Args:
        request (object): request.

    Returns:
        void
    """
    return render(request, 'login.html')


def login(request):
    """登入畫面
    Args:
        request (object): request.

    Returns:
        void
    """
    request.encoding = 'utf-8'
    if 'username' in request.POST and 'password' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            if user.is_staff:
                return redirect('/admin/home/')
            else:
                return redirect('/user/home/')
        else:
            return HttpResponse('使用者不存在')
    else:
        return render(request, 'login.html')
