# Generated by Django 2.0 on 2022-04-08 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180410_0911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='received_at',
        ),
    ]
