from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Contact form
    """
    
    class Meta:
        model = Contact
        fields = [
            'full_name',
            'email',
            'message'
        ]

    full_name = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control border-black rounded-0 profile-form-input',
            'placeholder': 'Full Name'
        })
    )

    email = forms.EmailField(
        required=True,
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control border-black rounded-0 profile-form-input',
            'placeholder': 'Your Email Address'
        })
    )

    message = forms.CharField(
        required=True,
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control border-black rounded-0 profile-form-input',
            'placeholder': 'How can we help?'
        })
    )
