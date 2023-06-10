from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from fiflo.decorators import is_allowed
from .models import UserGroup, Category, File
from .forms import *
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse


# Create your views here.
@login_required(login_url = 'login')
def index(request):
    return render(request,'base/home.html')



# USER GROUP VIEWS
@login_required(login_url = 'login')
@is_allowed(allowed_roles = ['admin'])
def user_group(request):
    q = request.GET.get('group-name-search') if request.GET.get('group-name-search') != None else ''
    groups = UserGroup.objects.filter(
        Q(name__icontains = q)
    )
    # groups = UserGroup.objects.all()
    context = {'groups': groups}
    return render(request,'user-group/index.html', context)


@login_required(login_url = 'login')
@is_allowed(allowed_roles = ['admin'])
def create_user_group(request):
    form = UserGroupForm()
    context = {'form': form}
    if request.method == 'POST':
        form = UserGroupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User group has been created successfully.')
            return redirect('user-group')
    return render(request, 'user-group/create.html',context)


@login_required(login_url = 'login')
@is_allowed(allowed_roles = ['admin'])
def group(request,pk):
    group = UserGroup.objects.get(id=pk)
    members = group.members.all()
    form = UserGroupForm(instance = group)
    files = File.objects.filter(group = pk)
    context = {'group':group,'form':form, 'members': members, 'files': files}
    if request.method == 'POST':
        form = UserGroupForm(request.POST, instance = group)
        if form.is_valid():
            form.save()
            messages.success(request, 'User group has been updated successfully.')
            return redirect('group', pk = group.id)
    return render(request,'user-group/group.html',context)


@login_required(login_url = 'login')
@is_allowed(allowed_roles = ['admin'])
def edit_group(request,pk):
    group = UserGroup.objects.get(id=pk)
    members = group.members.all()
    form = UserGroupForm(instance = group)
    context = {'group':group,'form':form, 'members': members}
    if request.method == 'POST':
        form = UserGroupForm(request.POST, instance = group)
        if form.is_valid():
            form.save()
            messages.success(request, 'User group has been updated successfully.')
            return redirect('group', pk = group.id)
    return render(request,'user-group/edit.html',context)


@login_required(login_url = 'login')
@is_allowed(allowed_roles = ['admin'])
def delete_group(request, pk):
    group = UserGroup.objects.get(id=pk)
    context = {'group': group}
    if request.method == 'POST':
        group.delete()
        messages.success(request, 'User group has been deleted successfully.')
        return redirect('user-group')
    return render(request, 'user-group/delete.html', context)




# CATEGORY VIEWS
def category(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'category/index.html',context)

def create_category(request):
    form = CategoryForm()
    context = {'form': form}
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category has been craeted successfully, add another category?')
            return redirect('create-category')
    return render(request, 'category/create.html', context)


def delete_category(request, pk):
    category = Category.objects.get(id=pk)
    context = {'category': category}
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category has been deleted successfully.')
        return redirect('categories')
    return render(request, 'category/delete.html', context)


def edit_category(request,pk):
    category = Category.objects.get(id=pk)
    form = CategoryForm(instance = category)
    context = {'category':category,'form':form}
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance = category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category has been updated successfully.')
            return redirect('categories')
    return render(request,'category/edit.html',context)


# FILES VIEWS
def files(request):
    files = File.objects.all()
    context = {'files':files}
    return render(request,'file/index.html',context)

def upload_file(request):
    form = UploadFileForm()
    context = {'form': form}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('files')
    return render(request,'file/upload.html',context)

def download_file(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    response = HttpResponse(file.file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{file.filename()}"'
    return response

def file(request,file_id):
    file = File.objects.get(id=file_id)
    groups = file.group.all()
    comments = file.comments.all()
    context = {'file':file,'groups':groups, 'comments': comments}
    return render(request, 'file/file.html', context)

def file_remove_group(request,file_id,group_id):
    file = File.objects.get(id=file_id)
    group = file.group.get(id = group_id)
    if request.method == 'POST':
        group.delete()
        messages.success(request, 'Group has been removed successfully.')
        return redirect('file', file_id = file_id)
    context = {'file':file,'group':group}
    return render(request, 'file/remove_group.html', context)

def delete_file(request,file_id):
    file = File.objects.get(id=file_id)
    if request.method == 'POST':
        file.delete()
        messages.success(request, 'File has been deleted successfully.')
        return redirect('files')
    context = {'file':file}
    return render(request, 'file/delete.html', context)