# Generated by Django 4.1.5 on 2023-01-14 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта')),
                ('is_active', models.BooleanField(default=False, verbose_name='Признак активности пользователя')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Пользователь администратор')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]