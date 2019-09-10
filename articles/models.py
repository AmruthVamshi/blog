from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Article(models.Model):
	title=models.CharField(max_length=100)
	slug=models.SlugField()
	body=models.TextField()
	date=models.DateField(auto_now_add=True)
	thumb=models.ImageField(blank=False,upload_to='media/')
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		return self.title
	def reduce(self):
		return self.body[:20] + "...."
	def titleReduce(self):
		return self.title[:8]+".."
	def deleteurl(self):
		return reverse('articles:delete',kwargs={'slug':self.slug})