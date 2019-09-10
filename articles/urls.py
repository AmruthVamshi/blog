from django.urls import path
from . import views

app_name='articles'

urlpatterns=[
	path('',views.home,name='list'),
	path('create',views.create,name='create'),
	path('myblogs',views.myblogs,name='myblogs'),
	path('delete/<str:delete_post>',views.delete,name='delete'),
	path('edit/<str:edit_post>',views.edit,name='edit'),
	path('<str:slug>',views.exp,name='details'),
]