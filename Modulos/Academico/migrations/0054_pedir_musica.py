# Generated by Django 3.1.4 on 2021-05-05 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Academico', '0053_delete_pedir_musica'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedir_Musica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedir', models.PositiveSmallIntegerField()),
                ('Fecha_Solicitado', models.DateTimeField(default=django.utils.timezone.now)),
                ('Fecha_a_Pedir', models.DateField(default=django.utils.timezone.now)),
                ('Fecha_Limite', models.DateField(default=django.utils.timezone.now)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.inv_musica')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HMusi', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
