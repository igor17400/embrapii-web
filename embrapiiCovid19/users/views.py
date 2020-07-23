from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import User
from .forms import UserForm

class UserListView(ListView):
    model = User 
    template_name = 'home.html'

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'

def UserCreate(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserForm()
    return render(request, "user_new.html", {"form": form})

def UserEdit(request, id):
    
    user = get_object_or_404(User, pk=id)
    if request.method == "POST":
        
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()

            return redirect("home")
    else:
        form = UserForm(instance=user)
    return render(request, "user_edit.html", {"form": form})

def UserDelete(request, id):
    
    user = get_object_or_404(User, pk=id)
    if request.method == "POST":
        user.delete()
        return redirect("home")
    else:
        return render(request, "user_delete.html", {"user": user})