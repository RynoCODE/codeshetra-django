from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import razorpay
from codeshetra import settings
from django.contrib.auth.models import User
from .models import credit

def student_dashboard(request):
    return render(request, 'student_dashboard.html')
def teacher_dashboard(request):
    return render(request, "teacher-dashboard.html")