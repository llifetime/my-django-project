from django.contrib import admin
from .models import Category, Product, Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Админ-панель для категорий"""
    list_display = ('name', 'description')
    list_filter = ('name',)
    search_fields = ('name', 'description')
    prepopulated_fields = {}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админ-панель для товаров"""
    list_display = (
        'name',
        'category',
        'price',
        'is_published',
        'created_at'
    )
    list_filter = ('category', 'is_published', 'created_at')
    search_fields = ('name', 'description', 'category__name')
    list_editable = ('price', 'is_published')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'description', 'category', 'price')
        }),
        ('Дополнительная информация', {
            'fields': ('image', 'is_published')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Админ-панель для контактов"""
    list_display = ('name', 'email', 'created_at', 'is_processed')
    list_filter = ('is_processed', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_editable = ('is_processed',)
    readonly_fields = ('name', 'email', 'message', 'created_at')
    fieldsets = (
        ('Информация о сообщении', {
            'fields': ('name', 'email', 'message', 'created_at')
        }),
        ('Статус обработки', {
            'fields': ('is_processed',)
        }),
    )

    def has_add_permission(self, request):
        """Запрещает добавление контактов через админку"""
        return False