from django.contrib import admin
from django.utils.html import format_html
from .models import Category, SubCategory, Product, NewsEvent, NewsImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['order']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'image_preview', 'order']
    list_filter = ['category']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['order']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:50px;border-radius:4px;"/>', obj.image.url)
        return "No Image"
    image_preview.short_description = "Preview"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'subcategory', 'image_preview', 'created_at']
    list_filter = ['subcategory__category', 'subcategory']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:50px;border-radius:4px;"/>', obj.image.url)
        return "No Image"
    image_preview.short_description = "Preview"


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 3
    fields = ['image', 'image_preview', 'caption', 'order']
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:80px;border-radius:6px;box-shadow:0 2px 8px rgba(0,0,0,0.15);"/>', obj.image.url)
        return "No Image Yet"
    image_preview.short_description = "Preview"


@admin.register(NewsEvent)
class NewsEventAdmin(admin.ModelAdmin):
    list_display = ['title', 'cover_preview', 'image_count', 'created_at', 'is_published']
    list_filter = ['is_published', 'created_at']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_published']
    inlines = [NewsImageInline]

    def cover_preview(self, obj):
        cover = obj.cover_image
        if cover:
            return format_html('<img src="{}" style="height:60px;border-radius:6px;box-shadow:0 2px 8px rgba(0,0,0,0.15);"/>', cover.url)
        return "No Images"
    cover_preview.short_description = "Cover"

    def image_count(self, obj):
        count = obj.images.count()
        return format_html('<span style="background:#0d6efd;color:#fff;padding:2px 10px;border-radius:12px;">{}</span>', count)
    image_count.short_description = "Images"
