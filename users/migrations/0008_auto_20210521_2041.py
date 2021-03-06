# Generated by Django 2.1.15 on 2021-05-21 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210519_1800'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='subject',
            new_name='topic',
        ),
        migrations.AlterField(
            model_name='subject',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
