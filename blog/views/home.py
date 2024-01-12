from django.shortcuts import render
from blog.models import ArticleModel
from django.core.paginator import Paginator
from django.db.models import Q

def index(request):
    articles = ArticleModel.objects.all()
    page = request.GET.get('page')
    search = request.GET.get('search')
    if search:
        articles = articles.filter(
            Q(title__icontains=search) |
            Q(content__icontains=search)
        ).distinct()

    paginator = Paginator(articles, 2)
    return render(request, 'blog/home.jinja', context={
        'articles':paginator.get_page(page),
    })