from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

def home(request):
    products_list = Product.objects.all()
    paginator = Paginator(products_list, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})
    
def base(request):
    return render(request, 'base.html')

# Create your views here.

