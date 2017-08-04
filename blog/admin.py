from django.contrib import admin

# Register your models here.
from django.utils.text import Truncator

from blog.models import Category, Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'create_date', 'preview_content')
    list_filter = ('author', 'category')
    date_hierarchy = 'create_date'
    ordering = ('create_date',)
    search_fields = ('title', 'contenu')

    fieldsets = (
        ('Général', {
            'fields': ('title', 'slug', 'author', 'category')
        }),
        ('Contenu de l\'article', {
            'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient.',
            'fields': ('content',)
        }),
        ('Images', {
            'fields': ('image',)
        })
    )
    prepopulated_fields = {'slug': ('title',)}

    def preview_content(self, article):
        return Truncator(article.content).chars(40, truncate='...')


admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
