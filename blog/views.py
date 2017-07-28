from blog.models import Article
from django.shortcuts import render, get_object_or_404
from .forms import ContactForm


def accueil(request):
    articles = Article.objects.all()
    return render(request, "blog/accueil.html", {"last_articles": articles})


def read_article(request, id_article, slug):
    article = get_object_or_404(Article, id=id_article, slug=slug)
    return render(request, "blog/read_article.html", {"article": article})


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['sender']
        resend = form.cleaned_data['resend']
        resend = True

    return render(request, 'blog/contact.html', locals())
