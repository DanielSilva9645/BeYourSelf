# Generated by Django 3.1.4 on 2021-04-24 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Academico', '0024_delete_invdeportes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inv_Deportes',
            fields=[
                ('codigo', models.CharField(default='', max_length=50)),
                ('materialess', models.CharField(default='', max_length=50, primary_key=True, serialize=False)),
                ('disponible', models.CharField(default='', max_length=5)),
                ('Fecha_Solicitado', models.DateField(default=django.utils.timezone.now)),
                ('Fecha_Limite', models.DateField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='in_Depo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]