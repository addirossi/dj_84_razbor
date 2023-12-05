import json

from main.models import Category, Product


def get_data():
    with open('./product.json', 'r') as file:
        data = json.load(file)
        category_name = data["category"]
        category = Category.objects.get_or_create(name=category_name)
        products = data['products']
        for prod in products:
            Product.objects.create(category=category, **prod)