from django.contrib import admin
from django.urls import path
from . import views
from . import video
from . import payment

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.sigin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('price/', payment.price, name='price'),


    #video call
    path('lobby/', video.lobby, name='lobby'),
    path('room/', video.room),
    path('get_token/', video.getToken),
    path('create_member/', video.createMember),
    path('get_member/', video.getMember),
    path('delete_member/', video.deleteMember),



]