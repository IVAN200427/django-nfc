from django.db import models

# Create your models here.
from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# =====================================================
# CATEGORY MODEL
# =====================================================

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)
# UPDATE THIS METHOD:
    def get_absolute_url(self):
        return reverse("category_products", kwargs={"category_slug": self.slug})

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def save(self, *args, **kwargs):
        """
        Automatically generate slug from category name.
        Example:
        Kitchen Mixers -> kitchen-mixers
        """
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# =====================================================
# PRODUCT MODEL
# =====================================================

class Product(models.Model):

    FINISH_CHOICES = [
        ('Polished Chrome', 'Polished Chrome'),
        ('Natural Brass', 'Natural Brass'),
        ('Matte Black', 'Matte Black'),
    ]

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    title = models.CharField(max_length=255)

    slug = models.SlugField(unique=True, blank=True)

    inlet_size = models.CharField(
        max_length=50,
        help_text="Example: 1/2 inch or 15mm"
    )

    finish = models.CharField(
        max_length=50,
        choices=FINISH_CHOICES
    )
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    technical_description = models.TextField()
    image = models.ImageField(
    upload_to='products/',
    default='default.jpg'   
)
    image_path = models.CharField(
    max_length=255,
    blank=True,
    help_text="Example: catalog/images/products/myimage.jpg"
)

    is_featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        """
        Automatically generate slug from product title.
        """
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# =====================================================
# QUOTE INQUIRY MODEL
# =====================================================

class QuoteInquiry(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='quote_inquiries'
    )

    customer_name = models.CharField(max_length=255)

    company_name = models.CharField(max_length=255)

    email = models.EmailField()

    phone_number = models.CharField(max_length=50)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Quote Inquiry"
        verbose_name_plural = "Quote Inquiries"

    def __str__(self):
        return f"{self.customer_name} - {self.product.title}"
    
class ContactMessage(models.Model):

    full_name = models.CharField(
        max_length=200
    )

    email = models.EmailField()

    subject = models.CharField(
        max_length=255
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ['-created_at']

    def __str__(self):

        return self.subject