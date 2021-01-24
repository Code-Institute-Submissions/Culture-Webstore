from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Contact
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages

import os
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')


def contact(request):
    """
    A view to add contact form info, return toast message
    and return to same page
    """

    full_name = request.POST.get('full_name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    user_id = request.user

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = Contact(
                full_name=full_name,
                email=email,
                message=message,
                user_id=user_id
            )
            form.save()
        else:
            form = Contact(
                full_name=full_name,
                email=email,
                message=message
            )
            form.save()
        
        send_mail(
            'New Contact Message from: '+ full_name,
            'Hey Admin,\n\nYou have a new message from ' 
            + full_name+'. '
            'Visit the admin dashboard to view.\n\nMany Thanks,\n\nCuture Couture',
            'culturewebstore@gmail.com',
            [EMAIL_HOST_USER],
            fail_silently=True
        )

        messages.success(request, f'Thanks for getting in touch {full_name}. We will be in contact with you soon!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {
        'form': ContactForm
    }
    return render(request, 'contact/contact.html', context)
