from django.contrib import admin

from .models import Category, IceCream, Topping, Wrapper

admin.site.empty_value_display = 'Не задано'


class IceCreamInline(admin.StackedInline):
    model = IceCream
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper',
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category',
    )
    search_fields = ('title',)
    list_filter = ('is_published',)
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)


# Регистрируем классы с настройками админки для моделей IceCream и Category.
admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Category, CategoryAdmin)

# Для Topping и Wrapper используется стандартный интерфейс админки.
admin.site.register(Topping)
admin.site.register(Wrapper)
