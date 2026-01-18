from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_list, name='todo'),
    path('todos/create/', views.create_todo, name='create'),
    path('todos/<int:pk>/', views.todo_detail, name='detail'),
    path('todos/<int:pk>/update/', views.update_todo, name='update'),
    path('todos/<int:pk>/delete', views.delete_todo, name='delete'),

]