# Generated by Django 5.0.6 on 2024-06-27 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_alter_user_managers_remove_user_date_joined_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
    ]
