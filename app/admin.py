from django.contrib import admin
from .models import Product, Topic, Departament, TopicProduct


# Register your models here.
class TopicProductInline(admin.TabularInline):
    model = TopicProduct


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug_name": ("name",)}
    inlines = [TopicProductInline]


class TopictAdmin(admin.ModelAdmin):
    inlines = [TopicProductInline]


class DepartamentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug_name": ("name",)}
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Topic, TopictAdmin)
admin.site.register(Departament, DepartamentAdmin)
