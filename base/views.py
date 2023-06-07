from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from fiflo.decorators import is_allowed

# Create your views here.
@login_required(login_url = 'login')
def index(request):
    return render(request,'base/home.html')

@is_allowed(allowed_roles = ['admin'])
def add_file(request):
    return render(request,'base/add_file.html')