from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError
from django.urls import reverse
from .models import User, Subject
from research.models import Topic

def profile(request):
    user_profile = User.objects.get(username=request.user.username)
    return render(request, "users/profile.html", {
    "user":user_profile
    })

def edit(request):
    topics = Topic.objects.all()
    return render(request, "users/edit.html", {"topics": topics})

def save_profile(request):
    if request.method == "POST":
        print(request.POST)
        first_name = request.POST["firstname"]
        last_name = request.POST["last_name"]
        user_type = request.POST["user_type"]
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.usertype = user_type
        user.save()
        if user_type == 'teacher':
            gettopic = Topic.objects.get(id = request.POST["topic"])
            user.topic = gettopic
            user.save()
        if user_type != 'teacher':
            user = request.user
            if user.topic != '':
                user.topic = None
                user.save()
        return redirect('users:profile')
    return redirect('users:login')


def login_view(request):
    if request.method == "POST":
        name = request.POST["name"]
        password = request.POST["password"]
        user = authenticate(request, username=name, password=password)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("main:home"))
        else:
            return render(request, "users/auth.sign-in.html", {
                "message": "Invalid username and/or password"
            })
    else:
        return render(request, "users/auth.sign-in.html")

def logout_view(request):
    logout(request)
    return redirect('main:home')

def register(request):
    if request.method == "POST":
        try:
            username = request.POST["name"]
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            email = request.POST["email"]
            try:
                subject = request.POST["subject"]
            except:
                subject = ''
            usertype = request.POST["usertype"]
            # Ensure password matches confirmation
            password = request.POST["password"]
            confirmation = request.POST["confirmation"]
            if password != confirmation:
                return render(request, "users/auth.register.html", {
                    "message": "Password must match"
                })
            try:
                if (usertype == "teacher"):
                    gettopic = Topic.objects.get(title = subject)
                    user = User.objects.create_user(username, email, password,
                    usertype=usertype, topic=gettopic, first_name=first_name, last_name=last_name)
                    user.save()
                    user.first_name = first_name
                    user.last_name = last_name
                    user.save()
                else:
                    user = User.objects.create_user(username, email, password,
                    usertype=usertype)
                    user.save()
                    user.first_name = first_name
                    user.last_name = last_name
                    user.save()
            except IntegrityError:
                return render(request, "users/auth.register.html", {
                "message": "Please Provide Unique Credentials"
                })
            login(request, user)
            return HttpResponseRedirect(reverse("main:home"))
        except:
            return render(request, "users/auth.register.html", {
                "message": "Please Provide Valid Credentials"
            })

    else:
        subjects = Topic.objects.all()
        return render(request, "users/auth.register.html", {
        "subjects": subjects
        })
