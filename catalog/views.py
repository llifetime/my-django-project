from django.shortcuts import render, redirect
from .models import Product, Category, Contact


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
        # Обработка формы
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            # Сохраняем контакт в базу
            Contact.objects.create(
                name=name,
                email=email,
                message=message
            )
            return redirect('catalog:contacts')

    return render(request, 'catalog/contacts.html')