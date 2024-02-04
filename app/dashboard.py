from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from codeshetra import settings
from django.contrib.auth.models import User
from .models import credit, interview
from django.contrib import messages
from django.core.mail import send_mail

@login_required
def student_dashboard(request):
    cred = credit.objects.get(user=request.user).credit
    credd = credit.objects.get(user=request.user)
    interviews = interview.objects.filter(user= request.user)
    
    if request.method == "POST":
        print(request.POST)
        if "Done" in request.POST:
            interview_id = request.POST.get('interview_id')
            if request.user.is_authenticated:
                interviews = interview.objects.get(pk=interview_id)
                print("Inter Received")
                if request.user == interviews.user:
                    interviews.done = True
                    interviews.save()
                    print("Interview Marked as done")
                    teacher = interviews.assigned_user
                    # teacher_cred = get_object_or_404(credit, user=teacher)
                    teacher_cred = credit.objects.get(user=teacher)
                    teacher_cred.credit += 1
                    teacher_cred.save()
                    print("Teacher credited")
                    messages.success(request, "Interview marked as done")
                    return redirect('student-dashboard')
                else:
                    messages.error(request, "You are not authorized to mark this interview as done")
                    return redirect('student-dashboard')
            else:
                messages.error(request, "You need to be logged in to mark an interview as done")
            return redirect('student-dashboard')
        if "req" in request.POST:
            topic = request.POST.get('topic')
            if topic:
                if cred >= 1:
                    interviews = interview.objects.create(user=request.user,
                                                        topic=request.POST.get('topic'),
                                                            date=request.POST.get('date'),
                                                            time=request.POST.get('time'),
                                                            duration=request.POST.get('duration'))
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
     
            
    return render(request, 'student_dashboard.html', {'cred':cred, 'interviews':interviews})


def student_action2(request, interview_id):
    interviews = interview.objects.get(pk=interview_id)
    if request.user == interviews.user:
        interviews.delete()
        cred = credit.objects.get(user=request.user)
        cred.credit += 1
        cred.save()
        messages.success(request, "Interview cancelled")
        return redirect('student-dashboard')
    
def student_action(request):
    if request.method == "POST":
        interview_id = request.POST.get('interview_id')
        if request.user.is_authenticated:
            interviews = interview.objects.get(pk=interview_id)
            print("Inter Received")
            if request.user == interviews.user:
                interviews.done = True
                interviews.save()
                print("Interview Marked as done")
                teacher = interviews.assigned_user
                # teacher_cred = get_object_or_404(credit, user=teacher)
                teacher_cred = credit.objects.get(user=teacher)
                teacher_cred.credit += 1
                teacher_cred.save()
                print("Teacher credited")
                messages.success(request, "Interview marked as done")
                return redirect('student-dashboard')
            else:
                messages.error(request, "You are not authorized to mark this interview as done")
                return redirect('student-dashboard')
        else:
            messages.error(request, "You need to be logged in to mark an interview as done")
        return redirect('student-dashboard')
    





@login_required
def teacher_dashboard(request):
    try:
        credd = credit.objects.get(user=request.user).credit
    except:
        profile = credit.objects.create(user=request.user, credit=0)
        profile.save()
        print("Credit created")
    interviews = interview.objects.all()
    
    return render(request, "teacher-dashboard.html",{'interviews': interviews, 'cred':credd,})

from django.core.mail import EmailMessage

def assign_interview(request, interview_id):
        interviews = interview.objects.get(pk=interview_id)
        if request.user.is_authenticated:
            # interview = get_object_or_404(interview, pk=interview_id)
            if request.method == "POST":
                roomid = request.POST.get('roomid')
                if roomid:
                    interviews.room_id = roomid
                    interviews.save()
                    messages.success(request, "Room ID assigned successfully")
                    subject="Interview Assigned"
                    message = f"Hi {interviews.user.username}, Your interview has been assigned to {interviews.assigned_user.username}. Please check your dashboard for more details.\n The Details:\nThe room number: {roomid}\nAssigned Interviewer: {interviews.assigned_user}\n\n Regards, CodeShetra"
                    from_email = settings.EMAIL_HOST_USER
                    to_list =  [interviews.user.email]
                    send_mail(subject,message,from_email,to_list,fail_silently=True)
                    email = EmailMessage(
                        subject,
                        message,
                        settings.EMAIL_HOST_USER,
                        [interviews.user.email],
                    )
                    email.fail_silently = True
                    email.send()
                    return redirect('teacher-dashboard')
                else:
                    messages.error(request, "Please fill in the room id")
                    return redirect('teacher-dashboard')

            if not  interviews.assigned_user:
                interviews.assigned_user = request.user
                interviews.save()
                messages.success(request, "Interview assigned successfully")
                


            else:
                messages.error(request, "Interview already assigned")
                # return redirect('teacher-dashboard')~
                # return JsonResponse({'error': 'Interview already assigned'}, status=400)
            return render(request, 'roomid.html')
        else:
            return JsonResponse({'error': 'User is not authenticated'}, status=401)
