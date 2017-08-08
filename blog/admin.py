from django.contrib import admin

# Register your models here.
from django.utils.text import Truncator

from blog.forms import ArticleForm
from blog.models import Category, Article


def duplicate(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()


duplicate.short_description = "Dupliquer les éléments selectionnés"


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'create_date', 'preview_content')
    list_filter = ('author', 'category')
    date_hierarchy = 'create_date'
    ordering = ('create_date',)
    search_fields = ('title', 'contenu')

    actions = [duplicate]
    prepopulated_fields = {'slug': ('title',)}
    form = ArticleForm

    def preview_content(self, article):
        return Truncator(article.content).chars(40, truncate='...')


admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
