from django.urls import path
from . import views

app_name='articles'

urlpatterns=[
	path('',views.home,name='list'),
	path('create',views.create,name='create'),
	path('myblogs',views.myblogs,name='myblogs'),
	path('<str:slug>',views.exp,name='details'),
	path('delete<str:delete_post>',views.exp,name='delete'),
]