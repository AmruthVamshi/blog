from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import blogForm
from django.urls import reverse
# Create your views here.
def home(request):
	articles_list=Article.objects.all().order_by('date')
	context={
		'articles':articles_list,
	}
	return render(request,'articles/home.html',context)
def exp(request,slug):
	if (slug[:6])=='delete':
		delete_post=slug[6:]
		delete=Article.objects.get(slug=delete_post)
		delete.delete()
		return redirect('articles:myblogs')
	articles_list=Article.objects.all().order_by('date')
	context={}
	for i in articles_list:
		if i.slug==slug:
			context={'articles_found':i}
			return render(request,'articles/articles_detail.html',context)
	else:
		return HttpResponse(articles_list[0].slug)
@login_required(login_url='/accounts/login/')
def create(request):
	if request.method=='POST':
		form=blogForm(request.POST,request.FILES)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.author=request.user
			instance.save()
			return redirect('articles:list')
	else:
		form=blogForm()
	return render(request,'articles/articles_create.html',{'form':form})
def myblogs(request):
	myblogs=Article.objects.filter(author=request.user)
	print(myblogs)
	context={
		'myblogs':myblogs,
	}
	return render(request,'articles/myblog.html',context)
	