from django.shortcuts import render, get_object_or_404
from .models import Product


def index(request):
    """Home page — shows a handful of featured products."""
    featured_products = Product.objects.filter(is_active=True)[:8]
    return render(request, 'shop/index.html', {
        'featured_products': featured_products,
    })


def product_grid(request):
    """Shop page — lists every active product from the database."""
    products = Product.objects.filter(is_active=True)
    return render(request, 'shop/product_grid.html', {
        'products': products,
    })


def product_details(request, slug):
    """Single product page, looked up by its slug."""
    product = get_object_or_404(Product, slug=slug, is_active=True)
    related_products = Product.objects.filter(is_active=True).exclude(pk=product.pk)[:4]
    return render(request, 'shop/product_details.html', {
        'product': product,
        'related_products': related_products,
    })


def cart(request):
    return render(request, 'shop/cart.html')


def checkout(request):
    return render(request, 'shop/checkout.html')


def wishlist(request):
    return render(request, 'shop/wishlist.html')


def login_view(request):
    return render(request, 'shop/login.html')


def contact(request):
    return render(request, 'shop/contact.html')
