from django.shortcuts import render
from .models import Products
from .forms import InsertNewProduct
# Create your views here.
def home(request):
    queryset=Products.objects.all()
    context={
        'qs':queryset,
    }
    return render(request,'home.html',context)
def html_insert(request):
    form=InsertNewProduct()
    return render(request,'insert.html',{'form':form})

def insert(request):
    if request.method=='POST':
        # form=InsertNewProduct(request.POST or None)
        name=request.POST['product_name']
        price=request.POST['product_price']
        description=request.POST['product_des']
        quantity=request.POST['product_qun']
        category=request.POST['category']
        inser=Products(name=name,description=description,price=price,quantity=quantity,category=category)
        inser.save()
    else:
        form=InsertNewProduct()
    qs=Products.objects.all()
    context={
            'qs':qs,
    }
    return render(request,'home.html',context)
def delete(request,pk):
    qs=Products.objects.get(pk=pk)
    qs.delete()
    query_set=Products.objects.all()
    return render(request,'home.html',{'qs':query_set})
def update(request,pk):
    qs=Products.objects.get(pk=pk)
    context={
        'qs':qs,
    }
    return render(request,'update.html',context)
