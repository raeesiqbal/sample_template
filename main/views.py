from django.shortcuts import render, redirect


def home(request):
    if request.user.is_authenticated:
        return render(request, 'pages/home.html', context={'home': True})
    return redirect('users:login')


def about(request):
    if request.user.is_authenticated:
        return render(request, 'pages/about.html', context={'about': True})
    return redirect('users:login')


def contact(request):
    if request.user.is_authenticated:
        return render(request, 'pages/contact.html', context={'contact': True})
    return redirect('users:login')
