# Generated by Django 4.2.1 on 2023-05-23 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_managers_user_birthday_user_departments_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthdate', models.DateField(blank=True, default=None, null=True, verbose_name='Дата рождения')),
                ('university_name', models.CharField(blank=True, max_length=50, verbose_name='Учебное заведение')),
                ('university_year', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Курс')),
                ('job_experience', models.TextField(blank=True, verbose_name='Опыт работы')),
                ('skills', models.TextField(blank=True, verbose_name='Навыки')),
                ('departments', models.TextField(blank=True, verbose_name='Предпочитаемые направления стажировки')),
            ],
        ),
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.RenameField(
            model_name='user',
            old_name='patronymic',
            new_name='surname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='user',
            name='departments',
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='job_experience',
        ),
        migrations.RemoveField(
            model_name='user',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='user',
            name='university_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='university_year',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Является администратором'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='E-Mail'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('CANDIDATE', 'Кандидат'), ('INTERN', 'Стажер'), ('CURATOR', 'Куратор'), ('STAFF', 'Кадровый специалист'), ('MENTOR', 'Наставник')], default='CANDIDATE', max_length=16, verbose_name='Роль'),
        ),
        migrations.AddField(
            model_name='user',
            name='info',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.userinfo'),
        ),
    ]
