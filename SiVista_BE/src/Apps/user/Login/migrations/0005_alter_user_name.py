# Generated by Django 5.0.6 on 2024-07-01 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0004_alter_user_managers_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]