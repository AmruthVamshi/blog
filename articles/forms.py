from django import forms
from .models import Article
class blogForm(forms.ModelForm):
	class Meta:
		model=Article
		fields=[
			'title','slug','body','thumb'
		]