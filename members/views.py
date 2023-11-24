from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def members(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
def products_view(request):
    return render(request, 'products.html')
def index_view(request):
    return render(request, 'index.html')
def car1_view(request):
    return render(request, 'car1.html')
def car2_view(request):
    return render(request, 'car2.html')
def car3_view(request):
    return render(request, 'car3.html')
def car4_view(request):
    return render(request, 'car4.html')
def car5_view(request):
    return render(request, 'car5.html')
def car6_view(request):
    return render(request, 'car6.html')

