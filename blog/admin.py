from django.contrib import admin
from blog.models import CategoryModel, ArticleModel, CommentModel, ContactModel

@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','created_at')
    search_fields = ('title','content','author')

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'comment')
    search_fields = ('comment',)

@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'message')
    search_fields = ('email', 'message')

admin.site.register(CategoryModel)