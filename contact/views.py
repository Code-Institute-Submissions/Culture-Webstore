from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages

def contact(request):
    """
    A view to add contact form info, return toast message
    and return to same page
    """

    full_name=request.POST.get('full_name')
    email=request.POST.get('email')
    message=request.POST.get('message')
    user_id=request.user

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

        messages.success(request, f'Thanks for getting in touch {full_name}. We will be in contact with you soon!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {
        'form': ContactForm
    }
    return render(request, 'contact/contact.html', context)
