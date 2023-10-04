from django.urls import path #path function
from . import views 
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home,name = 'home'),
    # path('home/', views.home_view, name='home'),
    path('menu/', views.menu,name = 'menu'),
    path('about/',views.about,name = 'about'),
    path('events/',views.events, name = 'events'),
    path('login/',views.custom_login, name = 'login'),
    path('signup/',views.signup, name = 'signup'),
    path('profile/', views.profile, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add_to_cart/<int:donut_id>/', views.add_to_cart, name = 'add_to_cart'),
    path('check_authentication/', views.check_authentication, name='check_authentication'),
    path('cart/', views.cart_view, name='cart'),
    path('update_cart/', views.update_cart_view, name='update_cart'),
    path('clear_cart/', views.clear_cart_view, name='clear_cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('order_confirmation/', views.order_confirmation, name='order_confirmation'),
    path('custom_logout/', views.custom_logout, name='custom_logout'),
    path('custom_logout_success/', views.custom_logout_success, name='custom_logout_success'),
]

