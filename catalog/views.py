from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import ContactForm


def home(request):
    """Контроллер для домашней страницы"""
    products = Product.objects.filter(is_published=True)[:6]
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    """Контроллер для страницы контактов"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog:contacts')
    else:
        form = ContactForm()

    return render(request, 'catalog/contacts.html', {'form': form})