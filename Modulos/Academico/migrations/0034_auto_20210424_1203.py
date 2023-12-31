# Generated by Django 3.1.4 on 2021-04-24 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Academico', '0033_auto_20210424_0906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inv_musica',
            name='Fecha_Limite',
        ),
        migrations.RemoveField(
            model_name='inv_musica',
            name='Fecha_Solicitado',
        ),
        migrations.RemoveField(
            model_name='inv_musica',
            name='user',
        ),
        migrations.CreateModel(
            name='Pedir_Musica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedir', models.PositiveSmallIntegerField()),
                ('Fecha_Solicitado', models.DateField(default=django.utils.timezone.now)),
                ('Fecha_Limite', models.DateField()),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.inv_musica')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='in_musi', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
