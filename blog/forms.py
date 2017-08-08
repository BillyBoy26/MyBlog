from django import forms
from blog.models import Article
from blog.widgets import RichText


class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField(label="Votre adresse email")
    resend = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'content': RichText(attrs={'rows': 15, 'cols': 100}),
        }
