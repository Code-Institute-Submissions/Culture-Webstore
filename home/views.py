from django.shortcuts import render
from products.models import Product
# Create your views here.

def index(request):
    """A view to return the index page"""

    featured = Product.objects.filter(featured=True).order_by('price')[:4]

    context = {
        'featured_products': featured,
    }

    return render(request, 'home/index.html', context)