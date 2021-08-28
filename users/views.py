from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from .models import CustomUser
from .forms import LoginForm
from django.contrib.auth import login, authenticate, logout
"""
for assistance with display of user: https://www.youtube.com/watch?v=jYuGw7o1S0I
"""

# Create your views here.


def index(request):
    user = request.user
    return render(request, 'index.html', {'user': user})


# def account_detail(request, id):
#     user = CustomUser.objects.get(id=id)
#     return render(request, 'account_detail.html', {'user': user})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('home')))
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})


def logout_view(request):
    # logout(request)
    # return request(redirect(''))
    return HttpResponseRedirect(reverse('login'))
