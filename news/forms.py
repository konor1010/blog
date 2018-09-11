from django.forms import ModelForm
from .models import Comments

class CommentForm(ModelForm):
    """ форма комментариев """
    class Meta:
        model = Comments
        fields = ('text', )
