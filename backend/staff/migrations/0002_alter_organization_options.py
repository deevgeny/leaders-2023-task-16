# Generated by Django 4.2.1 on 2023-05-24 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organization',
            options={'verbose_name': 'Организация', 'verbose_name_plural': 'Организации'},
        ),
    ]