from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

app_name = 'toapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('todo/', views.toappView, name='todo'),
    path('addTodoItem/', views.addTodoView),
    path('deleteTodoItem/<int:i>/', views.deleteTodoView),
]
