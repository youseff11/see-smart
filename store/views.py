from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, SubCategory, Product, NewsEvent
from .forms import RegisterForm, LoginForm, ContactForm


def home(request):
    categories = Category.objects.prefetch_related('subcategories').all()
    latest_news = NewsEvent.objects.filter(is_published=True)[:3]
    context = {
        'categories': categories,
        'latest_news': latest_news,
    }
    return render(request, 'store/home.html', context)


def about(request):
    return render(request, 'store/about.html')


def products(request):
    categories = Category.objects.prefetch_related('subcategories').all()
    return render(request, 'store/products.html', {'categories': categories})


def product_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    subcategories = category.subcategories.all()
    return render(request, 'store/product_category.html', {
        'category': category,
        'subcategories': subcategories,
    })


def product_subcategory(request, cat_slug, sub_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    subcategory = get_object_or_404(SubCategory, slug=sub_slug, category=category)
    products_list = subcategory.products.all()
    return render(request, 'store/product_subcategory.html', {
        'category': category,
        'subcategory': subcategory,
        'products': products_list,
    })


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    return render(request, 'store/contact.html', {'form': form})


def news_list(request):
    events = NewsEvent.objects.filter(is_published=True).prefetch_related('images')
    return render(request, 'store/news.html', {'events': events})


def news_detail(request, slug):
    event = get_object_or_404(NewsEvent, slug=slug, is_published=True)
    return render(request, 'store/news_detail.html', {'event': event})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    return render(request, 'store/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Welcome back!')
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
    return render(request, 'store/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')
