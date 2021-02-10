from django.shortcuts import render, redirect
from .models import Question, Choices
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.tokens import default_token_generator
from django.db import connection
from .forms import RegesterForm


# Create your views here.
def auth_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/home/ home')
    else:
        messages.info("Invalid Username or Password")
        return HttpResponseRedirect('/online/login_user')


@login_required(login_url='/online/login_user')
def invalid_login(request):
    return render(request, 'login.html', context=None)


@login_required(login_url='/online/login_user')
def logged_in(request):
    return render(request, '/home/home', {'full_name': request.user.username})


@login_required(login_url='/online/login_user')
def logout(request):
    auth.logout(request)
    return render(request, 'logout.html', context=None)


class NewUserPage(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'new_user.html', context=None)


def register(request):
    form = RegesterForm(request.POST)
    if form.is_valid():
        user = form.save()
        request.session['username'] = request.POST.get('username', '')
        auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('/home/home')
    return render(request, 'new_user.html', {'form': form})


class UserPage(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'neww.html', context=None)


def lostPassword(request):
    return render(request, 'neww.html', context=None)


@login_required(login_url='/online/login')
def quiz_myth(request):
    data = Question.objects.raw("select * from online_question where category == 'myth';")
    opts = Question.objects.raw("select * from online_choice;")
    return render(request, 'quizM.html', {'data': data, 'opts': opts})


@login_required(login_url='/online/login')
def quiz_myth1(request):
    data1 = Question.objects.raw("sect * from online_question;")
    opts1 = Question.objects.raw("select * from online_choice;")
    return render(request, 'quizM1.html',{'data1': data1, 'opts1': opts1})

