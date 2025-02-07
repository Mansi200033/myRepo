# Generated by Django 5.0.6 on 2024-06-27 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(db_column='is_admin', default=False),
        ),
    ]
