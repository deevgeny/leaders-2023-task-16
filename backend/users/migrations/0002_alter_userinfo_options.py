# Generated by Django 4.2.1 on 2023-05-24 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': 'Информация о пользователе'},
        ),
    ]