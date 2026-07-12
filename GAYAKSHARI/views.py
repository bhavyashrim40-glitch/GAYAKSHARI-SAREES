from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Product

# 1. ಗ್ರಾಹಕರು ಲಾಗಿನ್ ಆದ ಮೇಲೆ ಕಾಣಿಸುವ ಮುಖ್ಯ ಪುಟ (Saree Grid)
@login_required(login_url='login') # ಲಾಗಿನ್ ಆಗದಿದ್ದರೆ ನೇರವಾಗಿ ಲಾಗಿನ್ ಪುಟಕ್ಕೆ ಕಳುಹಿಸುತ್ತದೆ
def home(request):
    products = Product.objects.all() 
    return render(request, 'home.html', {'products': products})

# 2. ಲಾಗಿನ್ ಪುಟದ ಪ್ರಕ್ರಿಯೆ (Login View)
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') # ಯಶಸ್ವಿಯಾಗಿ ಲಾಗಿನ್ ಆದ ಮೇಲೆ ಹೋಮ್ ಪೇಜ್‌ಗೆ ಹೋಗುತ್ತದೆ
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# 3. ಹೊಸ ಗ್ರಾಹಕರು ಖಾತೆ ತೆರೆಯಲು ಸೈನ್-ಅಪ್ ಪುಟ (Signup View)
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # ಅಕೌಂಟ್ ಕ್ರಿಯೇಟ್ ಆದ ಮೇಲೆ ಲಾಗಿನ್ ಪೇಜ್‌ಗೆ ಹೋಗುತ್ತದೆ
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# 4. ಲಾಗ್‌ಔಟ್ ಪ್ರಕ್ರಿಯೆ (Logout View)
def logout_view(request):
    logout(request)
    return redirect('login')

from django.shortcuts import get_object_or_404
from .models import SareeOrder, Product

def place_order_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        # ಫಾರ್ಮ್‌ನಿಂದ ವಿವರಗಳನ್ನು ಪಡೆಯುವುದು
        name = request.POST.get('customer_name')
        phone = request.POST.get('customer_phone')
        address = request.POST.get('shipping_address')
        
        # ಡೇಟಾಬೇಸ್‌ನ SareeOrder ಟೇಬಲ್‌ಗೆ ಸೇರಿಸುವುದು
        SareeOrder.objects.create(
            customer_name=name,
            phone_number=phone,
            shipping_address=address,
            saree_name=product.name
        )
        return render(request, 'success.html', {'product': product}) # ಆರ್ಡರ್ ಯಶಸ್ವಿಯಾದ ಪೇಜ್
    return render(request, 'order_form.html', {'product': product})