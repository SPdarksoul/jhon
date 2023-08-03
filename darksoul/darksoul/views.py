from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from migrate.models import contact
from django.contrib import messages

def homepage(request):
    return render(request, "index.html")
def homepage(request):
    data = {
        'title': 'Sanya Masson'}
    return render(request, "index.htmL", data)

def about(request):
    return render(request, "about.html")

def myservices(request):
    return render(request, "myservices.html")

def mywork(request):
    return render(request, "mywork.html")
def contact(request):
    if request.method =="POST":
        name = request.POST.get('name'), 
        # lastname = request.POST.get('lastname'),
        email = request.POST.get('email'),
        subject = request.POST.get('subject'),
        address = request.POST.get('adress'),
        contact = contact(name= name , email= email,subject = subject,address=address)
        contact.save()
        messages.success(request, "Massage has been sent")
    return render(request,"index.html")