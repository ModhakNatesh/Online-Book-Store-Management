from django.shortcuts import render
from django.contrib.auth.models import User, auth
from .models import landing_seller, landing_book

# Create your views here.
def index(request):
    SELLERS = landing_seller.objects.all()
    BOOKS = landing_book.objects.all()
    return render(request, "index.html", {'SELLERS': SELLERS, 'BOOKS': BOOKS})


