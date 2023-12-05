from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from main.models import Product, Category


def products_list(request):
    #?price_from=50000&price_to=100000 -> {'price_from': 50000, 'price_to': 100000}
    products = Product.objects.all()
    price_from = request.GET.get('price_from')
    price_to = request.GET.get('price_to')
    if price_from:
        products = products.filter(price__gte=price_from)
    if price_to:
        products = products.filter(price__lte=price_to)
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))
    template_name = 'list.html'
    categories = Category.objects.all()
    return render(request, template_name, {'products': products, 'categories': categories})


def products_by_category(request, category_id):
    category = get_object_or_404(Category, slug=category_id)
    products = category.products.all()
    template_name = 'categories.html'
    return render(request, template_name, {'products': products})
