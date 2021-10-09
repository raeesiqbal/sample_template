from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from research.models import Project, Topic, Idea
from users.models import User
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

from django.template.loader import render_to_string
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient
from portal.settings import SENDGRID_API_KEY, SENDER_EMAIL

# Create your views here.
def research(request):
    if request.user.is_authenticated:
        data = Project.objects.all()
        return render(request, 'research/research.html', {
        "research":data.order_by("-timestamp").all()
        })
    return redirect('users:login')

def research_detail(request, id):
    if request.user.is_authenticated:
        data = Project.objects.get(id = id )
        return render(request, 'research/researchdetail.html', {
        "research":data
        })
    return redirect('users:login')

def add_research(request):
    if request.user.is_authenticated:
        data = Topic.objects.all()
        return render(request, 'research/addresearch.html', {
        "Topics":data
        })
    return redirect('research:research')

def save_research(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            title = request.POST["title"]
            content = request.POST["editor1"]
            topic = request.POST["topic"]
            main_image = request.FILES["mainimage"]
            try:
                file = request.FILES["file"]
            except:
                file = ''
            get_topic = Topic.objects.get(title  = topic)
            user = request.user
            try:
                research = Project(user=user, title=title, content=content,
                topic=get_topic, file=file, main_image=main_image)
                research.save()
                return redirect('research:research')
            except:
                pass
    return redirect('users:login')

def edit_research(request, id):
    if request.user.is_authenticated:
        research = Project.objects.get(id = id)
        topics = Topic.objects.all()
        if research.user.id == request.user.id:
            return render(request, 'research/editresearch.html', {
            "research":research, "topics":topics
            })
        return render(request, 'research/editresearch.html')
    return redirect('research:research')

def save_edit_research(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            title = request.POST["title"]
            content = request.POST["editor1"]
            topic = request.POST["topic"]
            main_image = request.FILES["mainimage"]
            try:
                file = request.FILES["file"]
            except:
                file = ''
            get_topic = Topic.objects.get(title = topic)
            user = request.user
            try:
                research = Project.objects.get(id = id)
                research.title = title
                research.save()
                research.content = content
                research.save()
                research.topic = get_topic
                research.save()
                research.main_image = main_image
                research.save()
                research.file = file
                research.save()
                return redirect('research:research_detail', id)
            except:
                return redirect('research:edit_research', id)
    return redirect('users:login')

def delete_research(request, id):
    if request.user.is_authenticated:
        research = Project.objects.get(id = id)
        if request.user.id == research.user.id:
            research.delete()
            return redirect('research:research')
    return redirect('users:login' )

def drop_idea(request):
    if request.user.is_authenticated:
        topics = Topic.objects.all()
        return render(request, 'research/dropidea.html', {
        "topics":topics
        })
    return redirect('users:login')

def save_idea(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            title = request.POST["title"]
            content = request.POST["editor1"]
            topic = request.POST["topic"]
            get_topic = Topic.objects.get(title = topic)
            user = request.user
        # try:
            idea = Idea(user=user, title=title, content=content,
            topic=get_topic)
            teacher_emails = list(idea.topic.teachers.values_list('email', flat=True))
            if not teacher_emails:
                return render(request, "research/dropidea.html", {
                    "message": "No Teacher exists for this idea"
                })

            message = render_to_string('email/idea.html', {
                'user': user,
                'idea': idea
            })
            mail = Mail(from_email=SENDER_EMAIL, to_emails=teacher_emails,subject=idea.title, html_content=message)
            try:
                send_grid = SendGridAPIClient(SENDGRID_API_KEY)
                send_grid.send(mail)
            except:
                return render(request, "research/dropidea.html", {
                    "message": "There is some error, please try again."
                })
            return redirect('research:research')
    return redirect('users:login')

@csrf_exempt
def related_idea(request):
    if request.method == "POST":
        data = json.loads(request.body)
        project = Project.objects.filter(title__icontains = data.get("value"))
        projects = project.order_by("-timestamp").all()
        return JsonResponse([project.serialize() for project in projects], safe=False)

@csrf_exempt
def ajax(request):
    if request.method == "POST":
        data = json.loads(request.body)
        id = int(data.get("id"))
        return JsonResponse({
        'success': True,
        'url': reverse('research:research_detail', args=[id]),
    })
    return JsonResponse({ 'success': False })
