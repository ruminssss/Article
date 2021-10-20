from django.forms import ModelForm

from .models import Art
from .models import Comment

class ArtForm(ModelForm):
    class Meta:
        model = Art
        fields = ('title', 'content', 'author')

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'author', 'art')