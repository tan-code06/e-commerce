from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.product_grid, name='product_grid'),
    path('product/<slug:slug>/', views.product_details, name='product_details'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('login/', views.login_view, name='login'),
    path('contact/', views.contact, name='contact'),
]
