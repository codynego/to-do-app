from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Todo
from .forms import TodoForm, LoginForm, SignupForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        user = request.user
        todolist = Todo.objects.filter(user=user)
        context = {
        'todolist': todolist,
        'user': user
        }
        return render(request, 'home.html', context)
    else:
        return redirect('login')

def todo_create(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
        }
    return render(request, 'todo_create.html', context)

def todo_detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {
        'todo': todo
        }
    return render(request, 'todo_detail.html', context)

def login(request):
    login = LoginForm()
    if request.method == 'POST':
        login = LoginForm(request.POST)
        if login.is_valid():
            username = login.cleaned_data.get('username')
            password = login.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('/')
            else:
                login.add_error(None, 'Invalid credentials. Try again.')
    else:
        login = LoginForm()
    context = {
        'login': login
        }
    return render(request, 'login.html', context)

def signup(request):
    signup = SignupForm()
    if request.method == 'POST':
        signup = SignupForm(request.POST)
        if signup.is_valid():
            signup.save()
            return redirect('home')
    context = {
        'signup': signup
        }
    return render(request, 'signup.html', context)

    # a login form that will allow the user to login to the site and see their todo list (if they have one)


    # a signup form that will allow the user to create a new account and login to the site (if they have one)

