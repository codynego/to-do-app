from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todo/create/', views.todo_create, name='todo_create'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]