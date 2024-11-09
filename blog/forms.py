from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo']
        widgets = {
            'conteudo': forms.Textarea(attrs={'rows': 5}),  # Personalize o widget se necessário
        }