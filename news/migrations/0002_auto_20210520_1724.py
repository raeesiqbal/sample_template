# Generated by Django 2.1.15 on 2021-05-20 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new',
            old_name='mainimage',
            new_name='main_image',
        ),
        migrations.RenameField(
            model_name='new',
            old_name='minidetail',
            new_name='mini_detail',
        ),
        migrations.RenameField(
            model_name='new',
            old_name='newsuser',
            new_name='news_user',
        ),
        migrations.AlterField(
            model_name='media',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='new',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
