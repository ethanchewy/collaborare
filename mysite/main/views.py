from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PDF
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewUserForm

# Create your views here.
def homepage(request):
    current_user = request.user
    lists_of_counts = []
    for p in PDF.objects.all():
        print(p)
        if current_user in p.users.all():
            lst = []
            for i in range(p.images_count):
                lst.append(i+1)
            lists_of_counts.append(lst)
    print(lists_of_counts)
    return render(request = request,
                  template_name='main/home.html',
                  context = {"pdfs":PDF.objects.all, "counts":lists_of_counts})

# COMPLETE CREDIT GOES TO:
# https://pythonprogramming.net/user-login-logout-django-tutorial/?completed=/messages-django-tutorial/
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})
