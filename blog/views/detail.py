from django.shortcuts import render, get_object_or_404
from blog.models import ArticleModel

def detail(request, slug):
    article = get_object_or_404(ArticleModel, slug=slug)
    comments = article.comments.all()
    return render(request, 'blog/detail.jinja', context={
        'article':article,
        'comments':comments,
    })