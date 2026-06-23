from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import Category, Product
from .forms import QuoteInquiryForm
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import (
    QuoteInquiryForm,
    ContactMessageForm)

from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Product

def product_list(request):
    products = Product.objects.all()

    return render(
        request,
        'catalog/product_list.html',
        {
            'products': products
        }
    )


def robots_txt(request):
    content = render_to_string("robots.txt")
    return HttpResponse(content, content_type="text/plain")
def homepage(request):

    featured_products = Product.objects.filter(
        is_featured=True
    )[:6]

    categories = Category.objects.all()

    context = {
        'featured_products': featured_products,
        'categories': categories,
    }

    return render(
        request,
        'catalog/homepage.html',
        context
    )
def search_products(request):

    query = request.GET.get('q')

    products = Product.objects.all()

    if query:

        products = products.filter(

            Q(title__icontains=query) |
            Q(inlet_size__icontains=query) |
            Q(technical_description__icontains=query) |
            Q(finish__icontains=query)

        )

    context = {
        'query': query,
        'products': products,
        'categories': Category.objects.all(),
    }

    return render(
        request,
        'catalog/search_results.html',
        context
    )
def category_products(request, category_slug):

    category = get_object_or_404(
        Category,
        slug=category_slug
    )

    products = Product.objects.filter(
        category=category
    )

    # FILTER BY FINISH

    finish = request.GET.get('finish')

    if finish:
        products = products.filter(
            finish=finish
        )

    # PAGINATION

    paginator = Paginator(products, 12)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'page_obj': page_obj,
        'finish': finish,
        'categories': Category.objects.all(),
    }

    return render(
        request,
        'catalog/category_products.html',
        context
    )


def product_detail(request, product_slug):

    product = get_object_or_404(
        Product,
        slug=product_slug
    )

    related_products = Product.objects.filter(
        category=product.category
    ).exclude(id=product.id)[:4]

    if request.method == 'POST':

        form = QuoteInquiryForm(request.POST)

        if form.is_valid():

            inquiry = form.save(commit=False)

            inquiry.product = product

            inquiry.save()

            # SEND EMAIL TO NFC SALES TEAM

            subject = f'New Bulk Quote Inquiry - {product.title}'

            message = f"""
A new quote inquiry has been submitted.

PRODUCT:
{product.title}

CUSTOMER NAME:
{inquiry.customer_name}

COMPANY:
{inquiry.company_name}

EMAIL:
{inquiry.email}

PHONE:
{inquiry.phone_number}

MESSAGE:
{inquiry.message}
"""

            send_mail(
                subject,
                message,
                'noreply@nfcindustrial.com',
                ['sales@nfcindustrial.com'],
                fail_silently=False,
            )

            # CUSTOMER CONFIRMATION EMAIL

            customer_subject = (
                'We Received Your Quote Inquiry - NFC Industrial'
            )

            customer_message = f"""
Dear {inquiry.customer_name},

Thank you for contacting Non-Ferrous Casting (NFC).

We have received your inquiry regarding:

{product.title}

Our sales team will review your request and contact you shortly.

Regards,
Non-Ferrous Casting (NFC)
50 Galloway Road
Norton, Zimbabwe
"""

            send_mail(
                customer_subject,
                customer_message,
                'noreply@nfcindustrial.com',
                [inquiry.email],
                fail_silently=False,
            )

            messages.success(
                request,
                'Your quote inquiry has been submitted successfully.'
            )

            return redirect(
                'product_detail',
                product_slug=product.slug
            )

    else:

        form = QuoteInquiryForm()

    context = {
        'product': product,
        'related_products': related_products,
        'form': form,
        'categories': Category.objects.all(),
    }

    return render(
        request,
        'catalog/product_detail.html',
        context
    )


def about_page(request):

    context = {
        'categories': Category.objects.all(),
        'page_title': 'About Non-Ferrous Casting (NFC)',
    }

    return render(
        request,
        'catalog/about.html',
        context
    )


def contact_page(request):

    if request.method == 'POST':

        form = ContactMessageForm(request.POST)

        if form.is_valid():

            contact_message = form.save()

            # ADMIN EMAIL

            subject = (
                f'New Contact Message - '
                f'{contact_message.subject}'
            )

            message = f"""
A new contact message was submitted.

NAME:
{contact_message.full_name}

EMAIL:
{contact_message.email}

SUBJECT:
{contact_message.subject}

MESSAGE:
{contact_message.message}
"""

            send_mail(
                subject,
                message,
                'noreply@nfcindustrial.com',
                ['vumimoyo@gmail.com'],
                fail_silently=False,
            )

            messages.success(
                request,
                'Your message has been sent successfully.'
            )

            return redirect('contact_page')

    else:

        form = ContactMessageForm()

    context = {
        'form': form,
        'categories': Category.objects.all(),
    }

    return render(
        request,
        'catalog/contact.html',
        context
    )