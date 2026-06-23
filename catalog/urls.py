from django.urls import path
from . import views




urlpatterns = [

    path('', views.homepage, name='homepage'),

    path(
        'about/',
        views.about_page,
        name='about_page'
    ),

    path(
        'contact/',
        views.contact_page,
        name='contact_page'
    ),

    path(
        'search/',
        views.search_products,
        name='search_products'
    ),

    path(
        'category/<slug:category_slug>/',
        views.category_products,
        name='category_products'
    ),

    path(
        'product/<slug:product_slug>/',
        views.product_detail,
        name='product_detail'
    ),
    path(
    'products/',
    views.product_list,
    name='product_list'
),
]