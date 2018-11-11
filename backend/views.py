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
    return render(request, 'admin/index.html')