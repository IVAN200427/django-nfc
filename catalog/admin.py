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
        "product_count",
        "slug",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "name",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    def product_count(self, obj):
        return obj.products.count()

    product_count.short_description = "Products"


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
       "featured_badge",
       "created_at",
)

    list_filter = (
        "category",
        "finish",
        "is_featured",
        "created_at",
    )

    search_fields = (
       "title",
       "category__name",
       "technical_description",
       "finish",
       "inlet_size",
       "created_at",
       )

    ordering = (
        "-created_at",

    )

    list_editable = (
        "is_featured",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    readonly_fields = (
        "image_preview_large",
        "created_at",
        "updated_at",
   )
    

    fieldsets = (

        ("📦 Product Information", {
            "fields": (
               "title",
               "slug",
               "category",
               "is_featured",
            )
       }),

        ("⚙️ Technical Specifications", {
          "fields": (
                "inlet_size",
                "finish",
                "technical_description",
            )
        }),

        ("🖼 Product Image", {
            "fields": (
                "image_path",
                "image_preview_large",
           ),
           "description": "Type the image filename exactly as it exists inside catalog/static/catalog/images/products/"
        }),
 
        ("📅 System Information", {
            "fields": (
                "created_at",
                "updated_at",
            ),
            "classes": ("collapse",),
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


    def featured_badge(self, obj):
       if obj.is_featured:
            return format_html(
               '<span style="background:#198754;color:white;padding:4px 10px;border-radius:20px;font-size:12px;">Featured</span>'
            )

       return format_html(
            '<span style="background:#6c757d;color:white;padding:4px 10px;border-radius:20px;font-size:12px;">Normal</span>'
        )

    featured_badge.short_description = "Status"

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

    search_fields = (
        "customer_name",
        "company_name",
        "email",
        "phone_number",
        "product__title",
    )

    list_filter = (
        "created_at",
        "product",
    )

    ordering = (
        "-created_at",
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
        "subject",
        "email",
        "created_at",
    )

    search_fields = (
        "full_name",
        "subject",
        "email",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
    )

# ==========================================================
# CUSTOM ADMIN BRANDING
# ==========================================================

admin.site.site_header = "NFC Industrial Administration"

admin.site.site_title = "NFC Admin"

admin.site.index_title = "Product & Customer Management"