from django import forms

from .models import Post


class CreatePostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ["title", "text", "image"]


class UpdatePostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ["title", "text", "image"]
