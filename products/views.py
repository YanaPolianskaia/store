from django.shortcuts import render, redirect
from products.models import Product
from .forms import ProductForm
# Create your views here.
def index(request):
    context = {
        'title':'Jewerly&Soul',
    }
    return render(request,'products/index.html', context)
def products(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products, 'title': 'Jewerly&Soul'})
def create(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            error = 'Форма неверная'
    form = ProductForm()
    data = {
        'form':form,
        'erroe':error
    }
    return render(request, 'products/create.html', data)