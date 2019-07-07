from django import forms
from .models import Comment


class Comment_Form(forms.ModelForm):
    parent = forms.CharField(widget=forms.HiddenInput(
                            attrs={'class': 'parent'}), required=False)

    class Meta:
        model = Comment
        fields = ('content',)