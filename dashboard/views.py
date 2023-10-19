from django.shortcuts import render,redirect
#we use decorators to compulsory the user to login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,request
from .models import Product
from .forms import ProductForm
# Create your views here.

@login_required
#this will not allow the user to access index page before login or register
def index(request):
    # return HttpResponse("<h1>This is the index page</h1>")
    #to return Httpresponse we have to mention request inside the function parameter

    return render(request,'dashboard/index.html')

@login_required
def staff(request):
    return render(request,'dashboard/staff.html')

@login_required
def product(request):
    items = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product') 
    else:
        form = ProductForm()
    # item = Product.objects.raw('SELECT * FROM dashboard_product')

    context ={
        'items':items,
        'form': form,
    }
    return render(request,'dashboard/product.html',context)

def product_delete(request,pk):
    item = Product.objects.get(id = pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request,'dashboard/product_delete.html')

def product_update(request, pk):
    # Get the product instance based on the primary key (pk)
    product = Product.objects.get(id=pk)

    if request.method == 'POST':
        # Populate the form with the data from the POST request
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        # Populate the form with the existing product data
        form = ProductForm(instance=product)

    context = {
        'form': form,
    }
    return render(request, 'dashboard/product_update.html', context)


@login_required
def order(request):
    return render(request,'dashboard/order.html')