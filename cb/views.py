from django.shortcuts import render

from django.http import JsonResponse
from django.shortcuts import render
from hugchat import hugchat
from hugchat.login import Login
from django.shortcuts import redirect

from django.shortcuts import render

def chatBot(request):
    if request.method == 'GET':
        # Assuming the user input is in the 'query' field of the request GET data
        query = request.GET.get("query")
        print("Query:", query)

        try:
            sign = Login("arka13", "Arkaprabha13")
            cookies = sign.login()
            # cookie_path_dir = "/migrations"
            # sign.saveCookiesToDir(cookie_path_dir)
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
            return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"error": "Invalid request method"})
    

def index(request):
    return render(request, 'student-help.html')
    

