from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
from django.db.models import Q

def news_home(request):
    search_query = request.GET.get('search', '')
    if search_query:
        news = Product.objects.filter(title__icontains = search_query)
    else:
        news = Product.objects.all()

    paginator = Paginator(news, 3)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
    }

    return render(request, 'paginator/news_home.html', {'page_object': page, 'is_paginated': is_paginated, 'next_url': next_url, 'prev_url': prev_url})
