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
    if request.user.is_authenticated and request.user.is_staff:
        return render(request, 'admin/index.html')
    else:
        return redirect('/auth/')