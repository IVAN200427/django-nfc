from django.contrib import admin
from django.utils.html import format_html
from django.templatetags.static import static
from .models import Category, Product, QuoteInquiry, ContactMessage


# ==========================================================
# CATEGORY ADMIN
# ==========================================================

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "slug",
    )

    search_fields = (
        "name",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }


# ==========================================================
# PRODUCT ADMIN
# ==========================================================

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "image_preview",
        "title",
        "category",
        "finish",
        "is_featured",
        "created_at",
    )

    list_filter = (
        "category",
        "finish",
        "is_featured",
    )

    search_fields = (
        "title",
        "technical_description",
        "inlet_size",
    )

    ordering = (
        "title",
    )

    list_editable = (
        "is_featured",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    readonly_fields = (
        "image_preview_large",
    )

    fieldsets = (
        ("Basic Information", {
            "fields": (
                "title",
                "slug",
                "category",
                "is_featured",
            )
        }),

        ("Specifications", {
            "fields": (
                "inlet_size",
                "finish",
                "technical_description",
            )
        }),

        ("Product Image", {
            "fields": (
                "image",
                "image_path",
                "image_preview_large",
            )
        }),
    )
    def image_preview(self, obj):
       if obj.image_path:
           return format_html(
               '<img src="{}" width="55" height="55" style="object-fit:cover;border-radius:6px;" />',
               static(obj.image_path)
           )
       return "-"
    image_preview.short_description = "Image"

    def image_preview_large(self, obj):
      if obj.image_path:
           return format_html(
               '<img src="{}" width="300" style="border-radius:10px;max-width:100%;" />',
               static(obj.image_path)
           )
      return "No image available"

    image_preview_large.short_description = "Preview"


# ==========================================================
# QUOTE INQUIRIES
# ==========================================================

@admin.register(QuoteInquiry)
class QuoteInquiryAdmin(admin.ModelAdmin):

    list_display = (
        "customer_name",
        "company_name",
        "product",
        "email",
        "phone_number",
        "created_at",
    )

    list_filter = (
        "created_at",
        "product",
    )

    search_fields = (
        "customer_name",
        "company_name",
        "email",
    )

    readonly_fields = (
        "created_at",
    )


# ==========================================================
# CONTACT MESSAGES
# ==========================================================

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "email",
        "subject",
        "created_at",
    )

    search_fields = (
        "full_name",
        "email",
        "subject",
    )

    readonly_fields = (
        "created_at",
    )