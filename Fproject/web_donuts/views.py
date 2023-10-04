from django.shortcuts import render,redirect
from itertools import groupby
from django.http import HttpResponse,JsonResponse 
from .models import Donut,CartItem,Order
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
import logging
from django.contrib.sessions.models import Session


logger = logging.getLogger(__name__)

def signup(request):
    if request.method == 'POST':
        # it passes the post data from the request
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # This will create a UserProfile associated with the newly created user.
            UserProfile.objects.create(user=user, full_name=user.username)
            # Logging the user in after registration,create a session for the user,
            login(request, user)
            logger.debug(f"User '{user.username}' successfully signed up and logged in.")
            return redirect('menu')  # Redirect to a successful page,pretty please
        else:
            logger.error("Form validation failed. Errors: %s", form.errors)
    else:
        # in case the method is not post a new instance of the UserCreationForm is created
        form = UserCreationForm() 

    return render(request, 'signup.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        # AuthenticationForm is part of Django's authentication system 
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('menu')  # Redirect to a success page,please
    else:
        # if it is incorrect a new form will appear
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def custom_logout(request):
    logout(request)

    return redirect('custom_logout_success')

def custom_logout_success(request):
    return render(request, 'custom_logout_success.html',{})


# takes a request, returns a response
def index(request):
    return HttpResponse("Hello, world. You're in the donut website.")


# def home (request):
#     return render(request,'home.html',{})

@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  
    else:
        form = UserProfileForm(instance=user_profile)

    user_email = request.user.email
    return render(request, 'profile.html', {'form': form,'user_profile': user_profile,'user_email': user_email })

def check_authentication(request):
    is_authenticated = request.user.is_authenticated
    return JsonResponse({'is_authenticated': is_authenticated})

# @login_required
# def add_to_cart(request, donut_id):

#     donut = Donut.objects.get(id=donut_id)
#     quantity = int(request.GET.get('quantity'))
#     print('Donut ID:', donut_id)
#     print('Quantity:', quantity)
#     cart_item, created = CartItem.objects.get_or_create(user=request.user, donut=donut)

#     if not created:
#         cart_item.quantity += quantity  
#         cart_item.save()

#     cart_count = request.user.cartitem_set.count()
#     return JsonResponse({'cart_count': cart_count})


@login_required
def cart_view(request):
    if not request.user.is_authenticated:
        return redirect('login')  
    
    cart_items = CartItem.objects.filter(user=request.user)
    
    total_price = sum(item.quantity * item.donut.price for item in cart_items)

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})
@login_required
def add_to_cart(request, donut_id):
    if not request.user.is_authenticated:
        return redirect('login')  

    donut = Donut.objects.get(id=donut_id)
    quantity = int(request.GET.get('quantity'))
    print('Donut ID:', donut_id)
    print('Quantity:', quantity)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, donut=donut)

    if not created:
        cart_item.quantity += quantity
        cart_item.save()

    cart_count = request.user.cartitem_set.count()
    return JsonResponse({'cart_count': cart_count})

def update_cart_view(request):
    if request.method == 'POST':
        for item in CartItem.objects.filter(user=request.user):
            quantity = request.POST.get(f'quantity_{item.id}')
            if quantity:
                item.quantity = int(quantity)
                item.save()
    return redirect('cart')

def clear_cart_view(request):
    if request.method == 'POST':
        CartItem.objects.filter(user=request.user).delete()
    return redirect('menu') 

@login_required
def checkout_view(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.quantity * item.donut.price for item in cart_items)

    if request.method == 'POST':
        print("DEBUG: Checkout request received") 
        try:
            cart_items.delete()
            print("DEBUG: Cart items deleted successfully")  
        except Exception as e:
            print(f"DEBUG: Error deleting cart items: {e}")  
        

        # try:
        
        #     session_key = request.session.session_key
        #     Session.objects.filter(session_key=session_key).delete()
        #     print(f"DEBUG: Session {session_key} deleted")  
        # except Exception as e:
        #     print(f"DEBUG: Error deleting session: {e}")  

        return redirect('order_confirmation')

    return render(request, 'checkout.html', {'cart_items': cart_items, 'total_price': total_price})


def home(request):
    return render(request, 'home.html')


# def menu(request):
#     donuts = Donut.objects.all()
#     return render(request, 'menu.html', {'donuts': donuts})

def menu(request):
    donuts = Donut.objects.all().order_by('category', 'name')  # Retrieve all donuts and order them by category and name
    donuts_by_category = {}
    
    for category, items in groupby(donuts, key=lambda x: x.category):
        donuts_by_category[category] = list(items)

    return render(request, 'menu.html', {'donuts_by_category': donuts_by_category})

def about(request):
    return render(request, 'about.html',{})

def events(request):
    return render(request, 'events.html',{})


def order_confirmation(request):
    return render(request, 'order_confirmation.html', {})

# def login(request):
#     return render(request,'login.html',{})

# def signup(request):
#     return render(request,'signup.html', {})



