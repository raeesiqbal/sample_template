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
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True, verbose_name='SubjectTitle:')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True, verbose_name='Title:')),
                ('subject', models.CharField(max_length=50, null=True, verbose_name='Subject:')),
                ('minidetail', models.CharField(blank=True, max_length=50, null=True, verbose_name='MiniDetail:')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Image')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Content')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='threaduser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]