# Generated by Django 4.2.6 on 2023-10-29 06:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='image/%Y', verbose_name='изображение'),
            preserve_default=False,
        ),
    ]
