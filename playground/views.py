from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q,F
from store.models import Product,OrderItem,Customer,Collection
from django.core.exceptions import ObjectDoesNotExist


def say_hello(request):
    query_set = Product.objects.filter(inventory=F('unit_price'))
    return render(request, 'hello.html', {'name': 'Aryan','products':list(query_set)})
