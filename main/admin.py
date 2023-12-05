from django.contrib import admin

from main.models import Category, Product, Order, OrderItem


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
    # prepopulated_fields = {'slug': ['name']}


class OrderItemsInline(admin.TabularInline):
    model = OrderItem
    fields = ['product', 'quantity']


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemsInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderItem)
