from django.shortcuts import render, HttpResponse
from django.core import serializers
from .models import Product
import json


def index_view(request):
	products = Product.objects.all()
	ctx = {'products': products}
	return render(request, 'miapp/index.html', ctx)


def contact_view(request):
	return render(request, 'miapp/contact.html')


def products_view(request):
	products = Product.objects.all()
	data = serializers.serialize("json", products)
	return HttpResponse(data, content_type='application/json')