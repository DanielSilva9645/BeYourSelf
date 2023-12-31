# Generated by Django 3.1.4 on 2021-05-31 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Principal', '0021_auto_20210528_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Titulo')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('start_time', models.DateTimeField(verbose_name='Fecha y Hora inicio')),
                ('end_time', models.DateTimeField(verbose_name='Fecha y Hora final   ')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
