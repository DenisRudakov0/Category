from django.shortcuts import render
from .models import Product

def news_home(request):
    news = Product.objects.all()
    return render(request, 'paginator/news_home.html', {'news': news})
