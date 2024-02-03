from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from codeshetra import settings
from django.contrib.auth.models import User
from .models import credit, interview
from django.contrib import messages
from hugchat import hugchat
from hugchat.login import Login


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

    if request.method == 'GET':
        # Assuming the user input is in the 'query' field of the request GET data
        query = request.GET.get("query")
        print("Query:", query)

        try:
            sign = Login("arka13", "Arkaprabha13")
            cookies = sign.login()
            cookie_path_dir = "/cookies"
            sign.saveCookiesToDir(cookie_path_dir)
            chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
            id = chatbot.new_conversation()
            chatbot.change_conversation(id)

            print("Before chatbot.chat call")
            bot_response = chatbot.chat(query)
            print("After chatbot.chat call")
            print("Aapi is Running! Bot -> ", bot_response)

            # Pass the response to the template context
            context = {'ANS': str(bot_response), 'anurag': 'anurag'}
            
            # Render the same HTML template with the updated context
            # return render(request, 'chatbot_project/index.html', context)
            # Instead of using redirect, use JsonResponse to send JSON response
            return JsonResponse({"Bot": str(bot_response)})

        except Exception as e:
            print("Error:", e)
            messages.error(request, str(e))
            # return JsonResponse({"error": str(e)})
            return redirect('student-dashboard')
    else:
        messages.error(request, "Invalid request method")
        # return JsonResponse({"error": "Invalid request method"})
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
