from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from codeshetra import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from . tokens import generate_token
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from . testing import *
from . models import UserProfile
from .models import credit



def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if is_valid_email(email) == False:
            messages.error(request, "Invalid email address.")
            return redirect('/signup')
        if User.objects.filter(username=username):
            messages.error(request, "Username alr Exists!!")
            return redirect('/signup')
        if User.objects.filter(email=email):
            messages.error(request, 'Email alr exists!!')
            return redirect('/signup')
        #password checking
        if password:
            if len(password) < 8:
                messages.error(request, "Password must be at least 8 characters long.")
                return redirect ('signup/') 
            if not any(char.isupper() for char in password):
                messages.error(request, "Password must contain at least one uppercase letter.")
                return redirect ('signup/')
            if not any(char.islower() for char in password):
                messages.error(request, "Password must contain at least one lowercase letter.")
                return redirect ('signup/')
            if not any(char.isdigit() for char in password):
                messages.error(request, "Password must contain at least one digit.")
                return redirect ('signup/')
            special_characters = r"[!@#$%^&*(),.?\":{}|<>]"
            if not re.search(special_characters, password):
                messages.error(request, "Password must contain at least one special character.")
                return redirect ('signup/')
        # password checking end
        if len(username)>10:
            messages.error(request, "Under 10 characters")
            return redirect('/signup')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('/signup')
        
        myuser = User.objects.create_user(username,email,password)
        myuser.is_active=False
        myuser.save()

        messages.success(request, "Your account has been successfully created. Check e-mail for activation!")

        # Email sending
        subject = 'Welcome to Codeshetra'
        message = "Hello " + myuser.username + "!! \n" + "Welcome to codeshetra!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \nPlease check your Spam inbox if you didn't receive any.  \n\nThanking You \nRohit"
        from_email = settings.EMAIL_HOST_USER
        to_list =  [myuser.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        current_site = get_current_site(request)
        email_subject = "Confirmation for Email Registration @ Codeshetra"
        hosst = settings.ALLOWED_HOSTS[0]
        message2 = render_to_string('email_confirmation.html',{
            'name': myuser.username,
            'domain': settings.ALLOWED_HOSTS[0],
            'uid':urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token':generate_token.make_token(myuser),
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()
        return redirect('signin')

    return render(request, 'signUp.html')

def sigin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if UserProfile.objects.filter(user=request.user).exists():    
                user_profile = UserProfile.objects.get(user=request.user)
                if user_profile.is_student == True:
                    return redirect("student-dashboard")
                else:
                    return redirect('teacher-dashboard')
            else:
                return redirect('dashboard')
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('signin')

    return render(request, 'signIn.html')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None
    
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('dashboard')
    else:
        return render(request, 'activation_failed.html')
@login_required
def signout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('signin')

@login_required
def dashboard(request):
    if request.method == "POST":
        print(request.POST)
        if "join" in request.POST:
            if credit.objects.filter(user=request.user).exists():
                return redirect("student-dashboard")
            else:
                return redirect("price")
    return render(request, 'dashboard.html')

