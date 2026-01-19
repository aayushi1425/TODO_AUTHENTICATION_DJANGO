from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from todoapp.forms import TodoForm
from todoapp.models import Todo

# Create your views here.

def home(request):
    return render(request, 'todoapp/home.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'User does not exist')
            return redirect('login')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
        else:
            login(request, user)
            return redirect('home')

    return render(request, 'todoapp/login.html')

def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.error(request, 'Username already exists')
            return redirect('register')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )

        user.set_password(password)
        user.save()
        messages.success(request, 'Account created successfully')
        return redirect('login')

    return render(request, 'todoapp/register.html')

def todo_page(request):

    item_list = Todo.objects.order_by('-date')
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    form = TodoForm()

    page = {
        "forms" : form,
        "list" : item_list,
        "title" : "Todo List",
    }
    return render(request, 'todoapp/todo_list.html', page)

# def todo_update(request):
#     return render(request, 'todo_list.html')

def todo_delete(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.success(request, 'Item deleted successfully')  
    return redirect('todo_list')

# def todo_view(request):
#     return render(request, 'todo_list.html')