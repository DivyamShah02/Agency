from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse_lazy

def home(request):
    return render(request,'index.html')
