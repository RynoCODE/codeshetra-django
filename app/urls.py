from django.contrib import admin
from django.urls import path
from . import views
from . import video
from . import payment, dashboard

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.sigin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('student-dashboard/', dashboard.student_dashboard, name='student-dashboard'),
    path('teacher-dashboard/', dashboard.teacher_dashboard, name='teacher-dashboard'),
    
    path('assign/<interview_id>/', dashboard.assign_interview, name='assign_interview'),

    # pricing
    path('price/', payment.price, name='price'),
    path('price/starter/', payment.starter, name='starter'),
    path('price/pro/', payment.pro, name='pro'),
    path('price/master/', payment.master, name='master'),
    path('success', payment.success, name='success'),
    path('payment/callback', payment.order_callback1, name='callback'),
    path('payment/callback1', payment.order_callback2, name='callback'),
    path('payment/callback2', payment.order_callback3, name='callback'),


    #video call
    path('lobby/', video.lobby, name='lobby'),
    path('room/', video.room),
    path('get_token/', video.getToken),
    path('create_member/', video.createMember),
    path('get_member/', video.getMember),
    path('delete_member/', video.deleteMember),


]