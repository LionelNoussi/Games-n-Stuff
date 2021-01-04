from django.shortcuts import render, redirect
from django.http import HttpResponse
from scanner.background.DBmanager import DBmanager, check
from scanner.background import send_message
from .forms import IDAndItem
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def homepage(request):
    if request.user.is_authenticated:
        #DBmanager.reload()
        if request.method == 'POST':
            form = IDAndItem(request.POST)
            if form.is_valid():
                DBmanager.process_form(form.cleaned_data["student_id"], form.cleaned_data["item"])
                for message in check.messageList:
                    send_message.make_toast(request, message[0], message[1], message[2])
                check.messageList.clear()

        return render(request, "scanner/home.html", {"form": IDAndItem, "itemList": check.itemList})
    else:
        return redirect("scanner:login")


def overview(request):
    if request.user.is_authenticated:
        missingDic = {"missing": DBmanager.create_overview()}
        return render(request, "scanner/overview.html", {"missingDic": missingDic})
    else:
        return redirect("scanner:login")


def history(request):
    if request.user.is_authenticated:
        entriesDic = {"missing": DBmanager.create_history()}
        return render(request, "scanner/history.html", {"missingDic": entriesDic})
    else:
        return redirect("scanner:login")


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("scanner:login")


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
                  template_name = "scanner/login.html",
                  context={"form":form})

