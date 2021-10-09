from django.shortcuts import render, redirect
from forums.models import Thread, Subject


def thread(request):
    if request.user.is_authenticated:
        threads = Thread.objects.all()
        return render(request, 'threads/threads.html', {
            "threads": threads.order_by("-timestamp").all()
        })
    return redirect('users:login')


def thread_detail(request, thread_id):
    if request.user.is_authenticated:
        get_thread = Thread.objects.get(id=thread_id)
        return render(request, 'threads/threaddetail.html', {
            "thread": get_thread
        })
    return redirect('users:login')


def add_thread(request):
    if request.user.is_authenticated:
        subjects = Subject.objects.all()
        return render(request, 'threads/addthread.html', {
            "subjects": subjects
        })
    return redirect('threads:thread')


def save_thread(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            title = request.POST["title"]
            content = request.POST["editor1"]
            image = request.FILES["image"]
            subject = request.POST["subject"]
            mini_detail = request.POST["minidetail"]
            user = request.user
            thread_save = Thread(user=user, title=title, content=content, image=image,
                                 subject=subject, mini_detail=mini_detail)
            thread_save.save()
            return redirect('forums:thread')
    return redirect('users:login')


def edit_thread(request, thread_id):
    if request.user.is_authenticated:
        get_thread = Thread.objects.get(id=thread_id)
        subjects = Subject.objects.all()
        if get_thread.user.id == request.user.id:
            return render(request, 'threads/editthread.html', {
                "thread": get_thread, "subjects": subjects
            })
        return render(request, 'threads/addthread.html')
    return redirect('threads:thread')


def save_edit_thread(request, thread_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            title = request.POST["title"]
            content = request.POST["editor1"]
            if 'image' in request.FILES:
                image = request.FILES["image"]
            subject = request.POST["subject"]
            mini_detail = request.POST["minidetail"]
            user = request.user
            try:
                get_thread = Thread.objects.get(id=thread_id)
                get_thread.title = title
                get_thread.save()
                if 'image' in request.FILES:
                    get_thread.image = image
                get_thread.save()
                get_thread.content = content
                get_thread.save()
                get_thread.mini_detail = mini_detail
                get_thread.save()
                get_thread.subject = subject
                get_thread.save()
                return redirect('forums:thread_detail', thread_id)
            except:
                return redirect('forums:add_thread')
    return redirect('users:login')


def delete_thread(request, thread_id):
    if request.user.is_authenticated:
        get_thread = Thread.objects.get(id=thread_id)
        if request.user.id == get_thread.user.id:
            get_thread.delete()
            return redirect('forums:thread')
    return redirect('users:login')
