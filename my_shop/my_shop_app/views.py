from django.shortcuts import render, redirect,get_object_or_404
from .models import Products,Category
from .forms import OrderForm,RegistrationForm,LoginForm
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, "Home page.html")

def catalog(request, category):
    context = {
            'products': Products.objects.filter(category__title=category),
            "category": Category.objects.all()
        }
    if category == "menu":
        context['products'] = Products.objects.all()
    return render(request, "Catalog.html", context)

def contacts(request):
    return render(request, "Contacts.html")

def about_us(request):
    return render(request, "About us.html")

def log_page(request):
        if request.method == 'POST':
            registration_form = RegistrationForm(request.POST)
            login_form = LoginForm(request.POST)

            if registration_form.is_valid():
                registration_form.save()

            if login_form.is_valid():
                username = login_form.cleaned_data['Username']
                password = login_form.cleaned_data['Password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
            return redirect('home')

        else:
            registration_form = RegistrationForm()
            login_form = LoginForm()

        return render(request, "Log page.html", {"registration_form": registration_form, "login_form": login_form})

def order_product(request):
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('home')

        else:
            form = OrderForm()

        return render(request, 'order_form.html', {'form': form})

def about_product(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    context = {
        'product': product
    }
    return render(request, "products_page.html", context)
