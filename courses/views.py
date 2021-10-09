from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from courses.models import Course, Subject, Video, Youtube
from users.models import User

# Create your views here.
def course(request):
    if request.user.is_authenticated:
        get_data = Course.objects.all()
        return render(request, 'courses/courses.html', {
        "data":get_data.order_by("-timestamp").all()
        })
    return redirect('users:login')


def course_detail(request, course_id):
    if request.user.is_authenticated:
        get_course = Course.objects.get(id = course_id )
        get_videos = Video.objects.all().filter(course = course_id)
        youtube_video = Youtube.objects.all().filter(course = get_course)
        return render(request, 'courses/coursedetail.html', {
        "course":get_course, "video":get_videos,
        "youtube_video":youtube_video
        })
    return render(request,'courses/coursedetail.html')

def add_course(request):
    if request.user.is_authenticated:
        subjects = Subject.objects.all()
        return render(request, 'courses/addcourse.html', {
        "subjects": subjects
        })
    return redirect('users:login')


def save_course(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user = request.user
            subject = request.POST["subject"]
            course_title = request.POST["title"]
            image = request.FILES["mainimage"]
            course_institute = request.POST["institute"]
            length = request.POST["length"]
            price = request.POST["price"]
            level = request.POST["level"]
            content = request.POST["content"]
            syllabus = request.POST["syllabus"]
            mini_detail = request.POST["minidetail"]
            course = Course(user = user, subject = subject, course_title = course_title,
            image = image, course_institute = course_institute, length = length,
            price = price, level = level, content = content, syllabus = syllabus,
            mini_detail=mini_detail)
            course.save()
            try:
                video = request.POST["youtube"]
                if (video != ''):
                    youtube_video = Youtube(course = course, video = video )
                    youtube_video.save()
            except:
                pass
            return redirect('courses:course')
    return redirect('users:login')


def edit_course(request, course_id):
    if request.user.is_authenticated:
        subjects = Subject.objects.all()
        get_course = Course.objects.get(id=course_id)
        if Youtube.objects.filter(course=get_course).exists():
            youtube_video = Youtube.objects.get(course=get_course)
        else:
            youtube_video = None
        if get_course.user.id == request.user.id:
            return render(request, 'courses/editcourse.html', {
            "course":get_course, "subjects":subjects, "youtube_video": youtube_video
            })
        return render(request, 'courses/addcourse.html')
    return redirect('users:login')


def save_edit_course(request, course_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            user = request.user
            subject = request.POST["subject"]
            course_title = request.POST["title"]
            if "mainimage" in request.FILES:
                image = request.FILES["mainimage"]
            course_institute = request.POST["institute"]
            length = request.POST["length"]
            price = request.POST["price"]
            level = request.POST["level"]
            content = request.POST["content"]
            syllabus = request.POST["syllabus"]
            mini_detail = request.POST["minidetail"]
            try:
                get_course = Course.objects.get(id = course_id)
                get_course.subject =subject
                get_course.save()
                get_course.course_title=course_title
                get_course.save()
                get_course.image=image
                get_course.save()
                get_course.course_institute=course_institute
                get_course.save()
                get_course.length=length
                get_course.save()
                get_course.price=price
                get_course.save()
                get_course.level=level
                get_course.save()
                get_course.content=content
                get_course.save()
                get_course.syllabus=syllabus
                get_course.save()
                get_course.mini_detail=mini_detail
                get_course.save()
                try:
                    video = request.POST["youtube"]
                    if (video != ''):
                        if (Youtube.objects.filter(course=get_course).exists()):
                            youtube_video = Youtube.objects.get(course=get_course)
                            youtube_video.delete()
                            youtube_video = Youtube(course=get_course, video=video)
                            youtube_video.save()
                        else:
                            youtube_video = Youtube(course=get_course, video=video)
                            youtube_video.save()
                except:
                    pass
                return redirect('courses:course_detail', course_id)
            except:
                return redirect('courses:edit_course', course_id)
    return redirect('users:login')


def delete_course(request, course_id):
    if request.user.is_authenticated:
        get_course = Course.objects.get(id = course_id)
        if request.user.id == get_course.user.id:
            get_course.delete()
            return redirect('courses:course')
    return redirect('users:login' )


def mini_details(request, course_id):
    if request.user.is_authenticated:
        get_course = Course.objects.get(id=course_id)
        return render(request, 'courses/minidetails.html', {
        "course":get_course
        })
    return redirect('users:login')


def add_video(request,course_id):
    if request.user.is_authenticated:
        return render(request, 'courses/addvideo.html', {
        "id":course_id
        })
    return redirect('users:login')


def save_video(request, course_id):
    if request.user.is_authenticated:
        video_title = request.POST["title"]
        video = request.FILES["video"]
        get_course = Course.objects.get(id=course_id)
        upload_video = Video(course=get_course, video = video, video_title=video_title)
        upload_video.save()
        return redirect('courses:course_detail', course_id)
    return redirect('users:login')


def delete_video(request, video_id, course_id):
    if request.user.is_authenticated:
        get_video = Video.objects.get(id = video_id)
        get_video.delete()
        return redirect('courses:course_detail', course_id)
    return redirect('users:login' )
