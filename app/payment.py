from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import razorpay
from codeshetra import settings
from django.views.decorators.csrf import csrf_exempt
client = razorpay.Client(auth=(settings.AUTH, settings.KEY))



# @login_required
def price(request):
    return render(request, 'pricing.html')

# @login_required
def starter(request):
    if request.method == "POST":
        client.order.create({
        "amount": 19900,
        "currency": "INR",
        "receipt": "receipt#1",
        "partial_payment": False,
        "notes": {
            "key1": "demo",
            "key2": "demo2"
        }
        })
    return render(request, 'starter.html')

# @login_required
def pro(request):
    if request.method == "POST":
        client.order.create({
            "amount": 59900,
            "currency": "INR",
            "receipt": "receipt#1",
            "partial_payment": False,
            "notes": {
                "key1": "demo",
                "key2": "demo2"
            }
            })
    return render(request, 'pro.html')

# @login_required
def master(request):
    if request.method == "POST":
        client.order.create({
            "amount": 99900,
            "currency": "INR",
            "receipt": "receipt#1",
            "partial_payment": False,
            "notes": {
                "key1": "demo",
                "key2": "demo2"
            }
            })
    return render(request, 'master.html')

@csrf_exempt
def success(request):
    return render(request, 'success.html')