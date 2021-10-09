from django.db import models
from users.models import User
from ckeditor.fields import RichTextField


class Subject(models.Model):
    subject_title = models.CharField(max_length=50, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject_title


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name="c_user",  null=True)
    subject = models.CharField(max_length=50, null=True, blank=True, verbose_name="Subject:")
    mini_detail = models.CharField(max_length=50, null=True, blank=True, verbose_name="Mini Detail:")
    course_title = models.CharField(max_length=50, null=True, verbose_name="Course_Title:")
    image = models.ImageField(null=True, blank=True, verbose_name="Image")
    course_institute = models.CharField(max_length=50, null=True, verbose_name="Institute:")
    length = models.IntegerField(null=True, verbose_name="length:")
    price = models.CharField(max_length=50, null=True, verbose_name="Price:")
    level = models.CharField(max_length=50, null=True, verbose_name="Level:")
    content = RichTextField(blank=True, null=True, verbose_name="Content")
    timestamp = models.DateTimeField(auto_now_add=True)
    syllabus = RichTextField(blank=True, null=True, verbose_name="Syllabus")

    def __str__(self):
        return self.course_title


class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None, related_name="course",  null=True)
    video = models.FileField(null=True, blank=True, verbose_name="video")
    video_title = models.CharField(max_length=50, null=True, verbose_name="Video_Title:")

    def __str__(self):
        return self.video_title


class Youtube(models.Model):
    course = models.ForeignKey(Course, verbose_name="Course", on_delete=models.CASCADE)
    video = models.CharField("Video id from youtube", null=True, blank=True, max_length=16, default=None)
