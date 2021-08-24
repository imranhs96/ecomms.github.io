from django.core import paginator
from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    Product_object=Products.objects.all()
    #Search Function
    item_name=request.GET.get('item_name') # name='item_name'
    if item_name != '' and item_name is not None:
        Product_object =Product_object.filter(title__icontains=item_name)#name__icontains
    
    
    #pagination
    
    paginator =Paginator (Product_object,4)
    page =request.GET.get('page')
    Product_object = paginator.get_page(page)

    return render(request,'shop\index.html',{'product_object' : Product_object})


def detail(request,Id):
    product_obj =Products.object.get(id=Id)#frist id is variable name and next id is function variable id
    return render (request,'shop/detail.html',{{'product_obj':product_obj}})
