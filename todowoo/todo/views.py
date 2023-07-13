from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
    else:
        try:
            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
        except IntegrityError:
            return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'That name has alrady been taken'})

        else:
            return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'password mismatch'})
