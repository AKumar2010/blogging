from django import forms
from django.forms import ModelForm
from MyBlog.models import *


class share_post_form(forms.Form):
	'''Form to be rendered to user when shared. '''
	name=forms.CharField()
	sbject=forms.CharField()
	email_to=forms.EmailField()
	comments=forms.CharField(widget=forms.Textarea,required=False)


class CommentForm(ModelForm):
	class Meta:
		model=Comment
		fields=['name','comment_content',]


class createPost_form(ModelForm):

	"""creating a new Post  """
	class Meta:
		model=Post
		fields=['title','author',"body","publish","status",]


