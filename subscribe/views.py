from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .models import Subscribers


def user_subscribe(request):
    """
    A view to add user to newsletter subscriber list, return toast message
    and return to same page
    """
    if request.method == 'POST':
        email = request.POST.get('subscriber_email')
        if Subscribers.objects.filter(email=email).exists():
            messages.error(request, f'Hey {email}, you\'re already on the list!')
        else:
            Subscribers.objects.create(email=email)
            messages.success(request, f'Success! {email}, you have been added to our newsletter.')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
