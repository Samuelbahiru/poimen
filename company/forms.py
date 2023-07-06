from django import forms
from . import models

class ResourceComment(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True, error_messages={'required': 'Title can not be empty'})
    email = forms.EmailField(required=True, error_messages={'required': 'Email can not be empty'})
    website =forms.URLField(required=False)
    comment = forms.CharField( required=True, widget=forms.TextInput())

    class Meta:
        model = models.Resource_Comment
        fields = ("name","email", "website", "comment")

class BlogComment(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True, error_messages={'required': 'Title can not be empty'})
    email = forms.EmailField(required=True, error_messages={'required': 'Email can not be empty'})
    website =forms.URLField(required=False)
    comment = forms.CharField( required=True, widget=forms.TextInput())

    class Meta:
        model = models.Blog_Comment
        fields = ("name","email", "website", "comment")
