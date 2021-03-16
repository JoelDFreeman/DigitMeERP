from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from ERP.models import *


def home(request):
    Orders = Order.objects.all()
    Companies = Company.objects.all()

    total_companies = Companies.count()

    total_orders = Orders.count()

    delivered =  Orders.filter(delivered=True).count()

    invoiced = Orders.filter(invoiced=True).count()

    paid = Orders.filter(paid=True).count()

    pending = Orders.filter(pending=True).count()

    context = {'orders':Orders, 'companies':Companies,
    'total_companies':total_companies, 'total_orders':total_orders,
    'delivered':delivered, 'invoiced':invoiced, 'paid':paid  }

    return render(request, 'ERP/home.html', context)

def Products(request):
    products = Product.objects.all()

    return render(request, 'ERP/products.html', {'products':products})  

def Orders(request):
    return render(request, 'ERP/orders.html')

def Companies(request):
    return render(request, 'ERP/companies.html')