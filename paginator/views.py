from django.shortcuts import render

def news_home(request):
    return render(request, 'paginator/news_home.html')
