from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings

def index(request):
    return render(request, 'welcome/index.html')

def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"Name: {name}\nEmail: {email}\n\n{message}"

        send_mail(
            subject,
            full_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.EMAIL_HOST_USER],  # Use the email from settings
            fail_silently=False,
        )
        return redirect('index')  # Redirect to a success page or back to the form
    return render(request, 'welcome/index.html')