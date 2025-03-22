from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'categories', 'audio_file', 'youtube_url']
        widgets = {
            'youtube_url': forms.URLInput(attrs={'placeholder': 'https://www.youtube.com/watch?v=XXXXXXXXXXX'}),
        }