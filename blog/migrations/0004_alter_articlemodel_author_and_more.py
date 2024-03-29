# Generated by Django 5.0.1 on 2024-01-13 19:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_contactmodel'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='category',
            field=models.ManyToManyField(related_name='article', to='blog.categorymodel'),
        ),
    ]
