from django.db import models
from users.models import User
from ckeditor.fields import RichTextField


class News(models.Model):
    news_user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name="NewsUser",  null=True)
    title = models.CharField(max_length=50, null=True, verbose_name="Title:")
    subject = models.CharField(max_length=50, null=True, blank=True, verbose_name="Subject:")
    mini_detail = models.CharField(max_length=50, null=True, blank=True, verbose_name="MiniDetail:")
    main_image = models.ImageField(null=True, blank=True, verbose_name="Image")
    content = RichTextField(blank=True, null=True, verbose_name="Content")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Media(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, default=None, related_name="news",  null=True)
    video = models.FileField(null=True, blank=True, verbose_name="NewsVideo")
    video_title = models.CharField(max_length=50, null=True, verbose_name="NewsvideoTitle:")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.video_title


class Subject(models.Model):
    subject_title = models.CharField(max_length=50, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject_title
