# Generated by Django 3.1 on 2020-10-27 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='address',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='tel',
        ),
        migrations.RemoveField(
            model_name='maincontent',
            name='image',
        ),
        migrations.AddField(
            model_name='contact',
            name='instagram',
            field=models.TextField(blank=True, max_length=50),
        ),
    ]
