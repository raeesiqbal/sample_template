# Generated by Django 3.2 on 2021-05-18 19:56

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=50, null=True, verbose_name='Subject:')),
                ('minidetail', models.CharField(blank=True, max_length=50, null=True, verbose_name='Mini Detail:')),
                ('course_title', models.CharField(max_length=50, null=True, verbose_name='Course_Title:')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Image')),
                ('course_institute', models.CharField(max_length=50, null=True, verbose_name='Institute:')),
                ('length', models.IntegerField(null=True, verbose_name='length:')),
                ('price', models.CharField(max_length=50, null=True, verbose_name='Price:')),
                ('level', models.CharField(max_length=50, null=True, verbose_name='Level:')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Content')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('syllabus', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Syllabus')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='c_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to='', verbose_name='video')),
                ('video_title', models.CharField(max_length=50, null=True, verbose_name='Video_Title:')),
                ('course', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course', to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_title', models.CharField(max_length=50, null=True, verbose_name='Subject_Title:')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
