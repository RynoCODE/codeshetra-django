from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from codeshetra import settings
from django.contrib.auth.models import User
from .models import credit, interview
from django.contrib import messages

@login_required
def student_dashboard(request):
    cred = credit.objects.get(user=request.user).credit
    credd = credit.objects.get(user=request.user)
    if request.method == "POST":
        if "req" in request.POST:
            topic = request.POST.get('topic')
            if topic:
                if cred >= 1:
                    interviews = interview.objects.create(user=request.user,
                                                        topic=request.POST.get('topic'),
                                                            date=request.POST.get('date'),
                                                            time=request.POST.get('time'),
                                                            duration=request.POST.get('duration'),
                                                            assigned_user="None")
                    interviews.save()
                    credd.credit -= 1
                    credd.save()
                    print("Database Updated")
                    messages.success(request, "Interview Scheduled. You will be receiving an email shortly with details")
                    return redirect('student-dashboard')
                else:
                    messages.error(request, "You do not have enough credits to schedule an interview")
                    return redirect('student-dashboard')
            else:
                messages.error(request, "Please fill in all the fields")
                return redirect('student-dashboard')
    return render(request, 'student_dashboard.html', {'cred':cred})

@login_required
def teacher_dashboard(request):
    try:
        credd = credit.objects.get(user=request.user).credit
    except:
        profile = credit.objects.create(user=request.user, credit=0)
        profile.save()
        print("Credit created")
    interviews = interview.objects.all()
    return render(request, "teacher-dashboard.html",{'interviews': interviews, 'cred':credd})



def assign_interview(request, interview_id):
        interviews = interview.objects.get(pk=interview_id)
        if request.user.is_authenticated:
            # interview = get_object_or_404(interview, pk=interview_id)
            if not  interviews.assigned_user:
                interviews.assigned_user = request.user
                interviews.save()
                messages.success(request, "Interview assigned successfully")
                return redirect('teacher-dashboard')
            else:
                messages.error(request, "Interview already assigned")
                return redirect('teacher-dashboard')
                # return JsonResponse({'error': 'Interview already assigned'}, status=400)
        else:
            return JsonResponse({'error': 'User is not authenticated'}, status=401)
