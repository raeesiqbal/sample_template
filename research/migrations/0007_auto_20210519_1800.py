# Generated by Django 3.2 on 2021-05-19 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0006_auto_20210519_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
