# Register your models here.
from django.contrib import admin
from .models import Category, Product, QuoteInquiry
from .models import ContactMessage

# =====================================================
# CATEGORY ADMIN
# =====================================================

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'slug',
    )

    prepopulated_fields = {
        'slug': ('name',)
    }

    search_fields = (
        'name',
    )


# =====================================================
# PRODUCT ADMIN
# =====================================================

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'inlet_size',
        'finish',
        'is_featured',
        'created_at',
    )

    list_filter = (
        'category',
        'finish',
        'is_featured',
    )

    search_fields = (
        'title',
        'inlet_size',
        'technical_description',
    )

    list_editable = (
        'is_featured',
    )

    prepopulated_fields = {
        'slug': ('title',)
    }


# =====================================================
# QUOTE INQUIRY ADMIN
# =====================================================

@admin.register(QuoteInquiry)
class QuoteInquiryAdmin(admin.ModelAdmin):

    list_display = (
        'customer_name',
        'company_name',
        'product',
        'email',
        'phone_number',
        'created_at',
    )

    list_filter = (
        'created_at',
        'product',
    )

    search_fields = (
        'customer_name',
        'company_name',
        'email',
        'phone_number',
    )

    readonly_fields = (
        'created_at',
    )
    
    
    
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'email',
        'subject',
        'created_at',
    )

    search_fields = (
        'full_name',
        'email',
        'subject',
    )

    readonly_fields = (
        'created_at',
    )