from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    body = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={
            "rows": "3",
            "placeholder": "Say something...."
        })
    )
    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'multiple': True
        })
    )

    class Meta:
        model = Post
        fields = ['body']


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={
            "rows": "3",
            "placeholder": "Say something...."
        })
    )

    class Meta:
        model = Comment
        fields = ['comment']


class ThreadForm(forms.Form):
    username = forms.CharField(label='', max_length=100,
                               widget=forms.TextInput(attrs={'placeholder': 'Search for people'}))


class MessageForm(forms.Form):
    message = forms.CharField(label='',
                              max_length=1000,
                              widget=forms.TextInput(attrs={'placeholder': 'Write a message'})
                        )


class ShareForm(forms.Form):
    body = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say something...'
        })
    )