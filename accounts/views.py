from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# Create your views here.
def signup(request):
	if request.method=="POST":
		form=UserCreationForm(request.POST or None)
		if form.is_valid():
			user=form.save()
			auth_login(request, user)
			return redirect('articles:list')
	else:
		form = UserCreationForm()
	return render(request,'accounts/signup.html',{'form':form})
def login(request):
	a=''
	if request.method=="POST":
		form=AuthenticationForm(data=request.POST or None)
		if form.is_valid():
			user=form.get_user()
			auth_login(request, user)
			if 'next' in request.POST:
				a=request.POST.get('next')
				return redirect(a)
			else:
				return redirect('articles:list')
	else:
		form = AuthenticationForm(request.POST or None)
	return render(request,'accounts/login.html',{'form':form,'a':a})
def logout(request):
	if request.method=="POST":
		auth_logout(request)
		return redirect('home')