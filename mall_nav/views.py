from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required

# Show login page ("/")
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('index')  # Redirect to mall navigation page
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

# Show mall navigation ("/index/") only after login
@login_required(login_url='/')
def index_view(request):
    return render(request, 'index.html')  # mall_nav/templates/index.html

# Logout user
def logout_view(request):
    logout(request)
    return redirect('/')  # Redirect to login page after logout
def map_view(request):
    return render(request, 'mall/map.html')