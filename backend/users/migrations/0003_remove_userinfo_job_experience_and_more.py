# Generated by Django 4.2.1 on 2023-06-06 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_userinfo_birthdate_alter_userinfo_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='job_experience',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='has_job_experience',
            field=models.BooleanField(null=True, verbose_name='Имеется опыт работы'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='has_volunteer_experience',
            field=models.BooleanField(null=True, verbose_name='Имеется опыт волонтерства'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='birthdate',
            field=models.DateField(blank=True, db_index=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='speciality',
            field=models.CharField(blank=True, max_length=60, verbose_name='Специальность'),
        ),
    ]
