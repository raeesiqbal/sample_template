from django.forms import ModelForm
from articles.models import Article

class AuthorForm(ModelForm):
    class Meta:
        model = Article
        fields = [
        'title', 'mini_detail', 'subject',
        'image', 'content'
        ]
        widgets = {
        'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'title'}),
        'mini_detail': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'mini detail'}),
        'subject': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'subject'}),
        'content': forms.Textarea(attrs={'class':'form-control', 'cols': 80, 'rows': 10})
        }
