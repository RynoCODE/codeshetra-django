from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import razorpay
from codeshetra import settings

def student_dashboard(request):
    return render(request, 'student_dashboard.html')