from django.db import models
from autoslug import AutoSlugField

class CategoryModel(models.Model):
    name = models.CharField(max_length=20, blank=False)
    slug = AutoSlugField(populate_from='name', unique=True)

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name