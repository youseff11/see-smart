from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('products/<slug:cat_slug>/', views.product_category, name='product_category'),
    path('products/<slug:cat_slug>/<slug:sub_slug>/', views.product_subcategory, name='product_subcategory'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news_list, name='news'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
