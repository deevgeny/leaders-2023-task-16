# Generated by Django 4.2.1 on 2023-06-08 17:17

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateCareerSchool',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='school', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('url', models.URLField(verbose_name='Ссылка для перехода на стороннюю платформу')),
                ('progress', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(limit_value=100)], verbose_name='Прогресс карьерной школы')),
            ],
            options={
                'verbose_name': 'Карьерная школа',
                'verbose_name_plural': 'Карьерная школа',
            },
        ),
        migrations.CreateModel(
            name='CandidateRequest',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='candidate_request', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('departments', models.TextField(verbose_name='Направления стажировки')),
                ('internship_source', models.TextField(verbose_name='Откуда узнали о стажировке')),
                ('schedule', models.PositiveIntegerField(verbose_name='График работы (кол-во часов)')),
                ('status', models.CharField(choices=[('WAITING', 'Ожидает рассмотрения'), ('ACCEPTED', 'Принята'), ('DECLINED', 'Отклонена')], default='WAITING', max_length=16, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Заявка кандидата',
                'verbose_name_plural': 'Заявки кандидатов',
            },
        ),

        migrations.CreateModel(
            name='CandidateTest',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='test', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('url', models.URLField(verbose_name='Ссылка для перехода на стороннюю платформу')),
                ('status', models.CharField(choices=[('PASS', 'Пройден'), ('FAIL', 'Не пройден'), ('WAITING', 'Ожидает прохождения')], default='WAITING', max_length=16, verbose_name='Результат тестирования')),
            ],
            options={
                'verbose_name': 'Тест кандидата',
                'verbose_name_plural': 'Тесты кандидатов',
            },
        ),
    ]
