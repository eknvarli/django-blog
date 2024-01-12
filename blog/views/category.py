from django.shortcuts import render, get_object_or_404
from blog.models import CategoryModel, ArticleModel
from django.core.paginator import Paginator

def category(request, category_slug):
    category = get_object_or_404(CategoryModel, slug=category_slug)
    articles = category.article.order_by('-id')
    page = request.GET.get('page')

    paginator = Paginator(articles, 2)
    return render(request, 'blog/category.jinja', context={
        'articles':paginator.get_page(page),
        'category':category.name,
    })