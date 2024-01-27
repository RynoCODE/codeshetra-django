from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import razorpay



@login_required
def price(request):
    return render(request, 'pricing.html')