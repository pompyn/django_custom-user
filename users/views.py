from django.shortcuts import render,HttpResponseRedirect, reverse
from .models import CustomUser
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import login, authenticate, logout
import os
import pwd

# Create your views here.


def index(request):
    usernames = CustomUser.objects.all()
    return render(request, 'index.html', {'usernames': usernames})


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
