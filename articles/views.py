from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from articles.models import Article, Subject
from users.models import User

# Create your views here.
def article(request):
    if request.user.is_authenticated:
        articles = Article.objects.all()
        return render(request, 'articles/articles.html', {
        "articles":articles.order_by("-timestamp").all()
        })
    return redirect('users:login')


def article_detail(request, article_id):
    if request.user.is_authenticated:
        get_article = Article.objects.get(id = article_id )
        return render(request, 'articles/articledetail.html', {
        "article":get_article
        })
    return redirect('users:login')


def add_article(request):
    if request.user.is_authenticated:
        subjects = Subject.objects.all()
        return render(request, 'articles/addarticle.html',{
        "subjects":subjects
        })
    return redirect('articles:article')


def save_article(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST["name"]
            content = request.POST["content"]
            image = request.FILES["image"]
            mini_detail = request.POST["minidetail"]
            subject = request.POST["subject"]
            user = request.user
            try:
                art = Article(user=user, title=name, content=content, image=image,
                subject=subject, mini_detail=mini_detail)
                art.save()
                return redirect('articles:article')
            except:
                pass
    return redirect('users:login')


def edit_article(request, article_id):
    if request.user.is_authenticated:
        get_article = Article.objects.get(id=article_id)
        if get_article.user.id == request.user.id:
            return render(request, 'articles/editarticle.html', {
            "article":get_article
            })
        return render(request, 'articles/addarticle.html')
    return redirect('articles:article')


def save_edit_article(request, article_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST["name"]
            content = request.POST["content"]
            if "image" in request.FILES:
                image = request.FILES["image"]
            mini_detail = request.POST["minidetail"]
            subject = request.POST["subject"]
            user = request.user
            try:
                art = Article.objects.get(id=article_id)
                art.title = name
                art.save()
                art.image = image
                art.save()
                art.content = content
                art.save()
                art.mini_detail = mini_detail
                art.save()
                art.subject = subject
                art.save()
                return redirect('articles:article_detail', article_id)
            except:
                return redirect('articles:article_detail', article_id )
    return redirect('users:login' )


def delete_article(request, article_id):
    if request.user.is_authenticated:
        get_article = Article.objects.get(id = article_id)
        if request.user.id == get_article.user.id:
            get_article.delete()
            return redirect('articles:article')
    return redirect('users:login' )
