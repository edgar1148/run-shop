from django.shortcuts import render, get_object_or_404

from .models import Category, ProductProxy


def products_view(request):
    """Вывод всех продуктов"""
    products = ProductProxy.objects.all()
    return render(request, 'shop/products.html', {'products': products})


def products_detail_view(request, slug):
    """Вывод конкретного продукта"""
    product = get_object_or_404(ProductProxy, slug=slug)
    return render(request, 'shop/products_detail.html', {'product': product})


def category_list(request, slug):
    """Вывод категории"""
    category = get_object_or_404(Category, slug=slug)
    products = ProductProxy.objects.select_related('category').filter(
        category=category)
    return render(
        request,
        'shop/category_list.html',
        {'category': category, 'products': products}
        )
