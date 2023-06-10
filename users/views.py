from django.shortcuts import render, redirect
from django.views import View
from . forms import UserRegistrationForm,UserUpdateForm
from django.contrib.auth.models import User,Group
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from fiflo.decorators import is_allowed
from django.contrib import messages

# Create your views here.
@login_required()
@is_allowed(allowed_roles=['admin'])
def index(request):
    users = User.objects.all().order_by('-date_joined')
    context = {'users':users}
    
    return render(request, 'auth/index.html', context)

@login_required()
@is_allowed(allowed_roles=['admin'])     
def register_user(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user_group = Group.objects.get(id = request.POST.get('role'))
            user.save()
            user.groups.add(user_group)
            messages.success(request, 'User has been registered successfully.')
            return redirect('users')     
    context = {'form': form}
    
    return render(request, 'auth/register_user.html', context)

@login_required()
@is_allowed(allowed_roles=['admin'])
def delete_user(request, pk):
    user = User.objects.get(id=pk)
    context = {'user': user}
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User has been deleted successfully.')
        return redirect('users')
    return render(request, 'auth/delete_user.html',context)  


@login_required()
@is_allowed(allowed_roles=['admin'])
def edit_user(request,pk):
    user = User.objects.get(id=pk)
    form = UserUpdateForm(instance = user)
    
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance = user)
        if form.is_valid():
            user_update = form.save(commit=False)
            
            if request.POST.get('group'):
                user_group = Group.objects.get(id = request.POST.get('role'))
            else:
                user_group = user.groups.all().first().id
            user_update.save()
            user_update.groups.remove(user.groups.all().first().id)
            user_update.groups.add(user_group)
            messages.success(request, 'User has been updated successfully.')
            return redirect('users')
    
    context = {'user': user, 'form':form}
            
    return render(request, 'auth/edit_user.html', context)
      
    