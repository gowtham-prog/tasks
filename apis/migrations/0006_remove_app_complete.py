# Generated by Django 4.2.2 on 2023-07-04 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0005_app_complete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='complete',
        ),
    ]