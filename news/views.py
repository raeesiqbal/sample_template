from django.shortcuts import render, redirect
from news.models import News, Media, Subject


def add_news(request):
    if request.user.is_authenticated:
        subjects = Subject.objects.all()
        return render(request, 'news/addnews.html', {
            "subjects": subjects
        })
    return redirect('users:login')


def save_news(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            title = request.POST["title"]
            content = request.POST["content"]
            main_image = request.FILES["mainimage"]
            subject = request.POST["subject"]
            mini_detail = request.POST["minidetail"]
            user = request.user
            try:
                new = News(news_user=user, title=title, main_image=main_image,
                           content=content, subject=subject, mini_detail=mini_detail)
                new.save()
                return redirect('news:news')
            except:
                return redirect('news:add_news')
    return redirect('users:login')


def news(request):
    if request.user.is_authenticated:
        get_news = News.objects.all()
        get_media = Media.objects.all()
        return render(request, 'news/news.html', {
            "news": get_news, "media": get_media
        })
    return redirect('users:login')


def news_detail(request, news_id):
    if request.user.is_authenticated:
        get_news = News.objects.get(id=news_id)
        get_news_media = Media.objects.all().filter(news=get_news)
        return render(request, 'news/newsdetail.html', {
            "news": get_news, "newsmedia": get_news_media
        })
    return redirect('users:login')


def edit_news(request, news_id):
    if request.user.is_authenticated:
        subjects = Subject.objects.all()
        get_news = News.objects.get(id=news_id)
        return render(request, 'news/editnews.html', {
            "new": get_news, "subjects": subjects
        })
        return render(request, 'articles/addarticle.html')
    return redirect('articles:article')


def save_edit_news(request, news_id):
    if request.user.is_staff or request.user.is_superuser:
        if request.method == "POST":
            title = request.POST["title"]
            content = request.POST["content"]
            if 'mainimage' in request.FILES:
                main_image = request.FILES["mainimage"]
            subject = request.POST["newssubject"]
            mini_detail = request.POST["minidetail"]
            try:
                get_news = News.objects.get(id=news_id)
                get_news.title = title
                get_news.save()
                get_news.content = content
                get_news.save()
                if 'mainimage' in request.FILES:
                    get_news.main_image = main_image
                get_news.save()
                get_news.subject = subject
                get_news.save()
                get_news.mini_detail = mini_detail
                get_news.save()
                return redirect('news:news_detail', news_id)
            except:
                return redirect('news:edit_news', news_id)
    return redirect('users:login')


def delete_news(request, news_id):
    if request.user.is_authenticated:
        get_news = News.objects.get(id=news_id)
        get_news.delete()
        return redirect('news:news')
    return redirect('users:login')


def add_news_video(request, news_id):
    if request.user.is_authenticated:
        return render(request, 'news/addnewsvideo.html', {
            "id": news_id
        })
    return redirect('users:login')


def save_news_video(request, news_id):
    if request.user.is_authenticated:
        video_title = request.POST["title"]
        video = request.FILES["video"]
        get_news = News.objects.get(id=news_id)
        upload_video = Media(news=get_news, video=video, video_title=video_title)
        upload_video.save()
        return redirect('news:news_detail', news_id)
    return redirect('users:login')


def delete_news_video(request, video_id, news_id):
    if request.user.is_authenticated:
        get_video = Media.objects.get(id=video_id)
        get_video.delete()
        return redirect('news:news_detail', news_id)
    return redirect('users:login')
