from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from decimal import Decimal
from .models import Order
from django.contrib.auth.decorators import login_required

def checkout_order(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        book_price = request.POST.get('book_price')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        name = request.POST.get('name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        country = request.POST.get('country')
        quantity = request.POST.get('quantity')
        subtotal = request.POST.get('subtotal')

        try:
            book_price = Decimal(book_price.strip('₹ '))
            quantity = int(quantity)
            subtotal = book_price * quantity
        except (ValueError, TypeError):
            raise ValidationError('Invalid book price or quantity')
        
        cod = True if request.POST.get('COD') == 'on' else False

        order = Order.objects.create(
            book_name=book_name,
            book_price=book_price,
            email=email,
            phone=phone,
            name=name,
            address=address,
            city=city,
            pincode=pincode,
            country=country,
            quantity=quantity,
            subtotal=subtotal,
            cod=cod
        )
        
    messages.success(request, 'Your order has been placed successfully!')
    return render(request, 'success.html')

def checkout_view(request):
    book_name = request.GET.get('book_name', '')
    book_price = request.GET.get('book_price', '')
    return render(request, 'checkout.html', {'book_name': book_name, 'book_price': book_price})

def landing_page(request):
    return render(request, 'checkout/landing_page.html')

def success_view(request):
    return render(request, 'checkout/success.html')

def orders(request):
    return render(request, 'checkout/orders.html')

@login_required
def order_details(request):
    if request.user.is_staff or request.user.is_superuser:
        orders = Order.objects.all()
        return render(request, 'orders.html', {'orders': orders})
    else:
        return HttpResponseRedirect('/') 
    


