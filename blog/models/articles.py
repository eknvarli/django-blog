from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from .categories import CategoryModel
from blog.abstract_models import DateAbstractModel

class ArticleModel(DateAbstractModel):
    title = models.CharField(max_length=50, blank=False)
    content = RichTextField()
    image = models.ImageField(upload_to='images/blog/')
    category = models.ManyToManyField(CategoryModel, related_name='article')
    author = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE, related_name='articles')
    slug = AutoSlugField(populate_from='title')

    class Meta:
        db_table = 'article'
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title