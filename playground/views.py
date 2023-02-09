from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product
# Create your views here.


def say_hello(request):
    queryset = Product.objects.filter(Q(inventory__lt=10) | Q(
        unit_price__lt=20))  # search for more: queryset api

    return render(request, 'hello.html', {'name': 'amir', 'products': list(queryset)})
