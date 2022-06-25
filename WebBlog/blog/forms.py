from dataclasses import fields
from django import forms
from .models import Comment, Post, Category

choices = Category.objects.all().values_list('name','name')
choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','body','snippet','header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control','placeholder':'Write tags'}),
            'author': forms.TextInput(attrs={'class': 'form-control','value':'','id':'username','type':'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder':'Blog post body'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control','placeholder':'Blog post snippet'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','body','snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control','placeholder':'Write tags'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder':'Blog post body'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control','placeholder':'Blog post snippet'}),
        
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        
        }