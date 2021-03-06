# Generated by Django 2.1.15 on 2021-05-19 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0005_auto_20210519_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name='Subject:'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='topic',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ideatopic', to='research.Topic'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name='Subject:'),
        ),
        migrations.AlterField(
            model_name='project',
            name='topic',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projectopic', to='research.Topic'),
        ),
    ]
