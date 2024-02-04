# cb/urls.py

from django.urls import path
from . import views

app_name = 'cb'

urlpatterns = [
    path('home/', views.chatBot, name='chatbot'),
    path('student_help/', views.index, name='student_help'),

    # other paths...
]
