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
            topic = request.POST.get('topic')
            if topic:
                interviews = interview.objects.create(user=request.user,
                                                    topic=request.POST.get('topic'),
                                                        date=request.POST.get('date'),
                                                        time=request.POST.get('time'),
                                                        duration=request.POST.get('duration'))
                interviews.save()
                messages.success(request, "Interview Scheduled. You will be receiving an email shortly with details")
                return redirect('student-dashboard')
            else:
                messages.error(request, "Please fill in all the fields")
                return redirect('student-dashboard')

    return render(request, 'student_dashboard.html', {'cred':cred})
def teacher_dashboard(request):
    return render(request, "teacher-dashboard.html")