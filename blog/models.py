from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    slug = models.CharField(max_length=100)
    content = models.TextField(null=True)
    create_date = models.DateField(auto_now_add=True, auto_now=False, verbose_name='Date de création')
    category = models.ForeignKey("Category")

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
