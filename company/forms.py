from django import forms
from . import models

class Comment_Form(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True, error_messages={'required': 'Title can not be empty'})
    email = forms.EmailField(required=True, error_messages={'required': 'email can not be empty'})
    website =forms.URLField(required=False)
    comment = forms.CharField(max_length=True, required=False, widget=forms.TextInput())

    class Meta:
        model = models.Blog_Comment
        fields = ("name","email", "website", "comment", "post")
