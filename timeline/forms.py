from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget = forms.Textarea()
        self.fields['text'].widget.attrs.update(
            placeholder='Deixe aqui um pensamento')
