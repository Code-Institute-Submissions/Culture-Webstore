from django.shortcuts import render


def about(request):
    """A view to return the about page"""

    return render(request, 'pages/about.html')


def faq(request):
    """A view to return the FAQ page"""

    return render(request, 'pages/faq.html')


def privacy_policy(request):
    """A view to return the Privacy Policy page"""

    return render(request, 'pages/privacy-policy.html')


def terms_conditions(request):
    """A view to return the Terms & Conditions page"""

    return render(request, 'pages/terms-conditions.html')
