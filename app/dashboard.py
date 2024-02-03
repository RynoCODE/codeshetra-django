from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import razorpay
from codeshetra import settings
from django.contrib.auth.models import User
from .models import credit, interview
from django.contrib import messages

def student_dashboard(request):
    cred = credit.objects.get(user=request.user).credit
    if request.method == "POST":
        if "req" in request.POST:
            interview = interview.objects.create(user=request.user, topic=request.POST['topic'], date=request.POST['date'], time=request.POST['time'], duration=request.POST['duration'])
            interview.save()
            messages.success(request, "Interview Scheduled. You will be receiving an email shortly with details")
            return redirect('student_dashboard')

    return render(request, 'student_dashboard.html', {'cred':cred})
def teacher_dashboard(request):
    return render(request, "teacher-dashboard.html")