from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout_view, name='checkout'),
    path('checkout_order/', views.checkout_order, name='checkout_order'),
    path('success/', views.success_view, name='success'),
    path('order_details/', views.order_details, name='order_details')
]

