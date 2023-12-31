# Generated by Django 3.1.4 on 2021-05-06 23:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Academico', '0058_auto_20210506_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedir_TA',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('pedir', models.PositiveSmallIntegerField()),
                ('Fecha_Solicitado', models.DateTimeField(default=django.utils.timezone.now)),
                ('Fecha_a_Pedir', models.DateField(default=django.utils.timezone.now)),
                ('Fecha_Limite', models.DateField(default=django.utils.timezone.now)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.inv_ta')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HTA', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pedir_Pintura',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('pedir', models.PositiveSmallIntegerField()),
                ('Fecha_Solicitado', models.DateTimeField(default=django.utils.timezone.now)),
                ('Fecha_a_Pedir', models.DateField(default=django.utils.timezone.now)),
                ('Fecha_Limite', models.DateField(default=django.utils.timezone.now)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.inv_pintura')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HPint', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pedir_Musica',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('pedir', models.PositiveSmallIntegerField()),
                ('Fecha_Solicitado', models.DateTimeField(default=django.utils.timezone.now)),
                ('Fecha_a_Pedir', models.DateField(default=django.utils.timezone.now)),
                ('Fecha_Limite', models.DateField(default=django.utils.timezone.now)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.inv_musica')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HMusi', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pedir_Foto',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('pedir', models.PositiveSmallIntegerField()),
                ('Fecha_Solicitado', models.DateTimeField(default=django.utils.timezone.now)),
                ('Fecha_a_Pedir', models.DateField(default=django.utils.timezone.now)),
                ('Fecha_Limite', models.DateField(default=django.utils.timezone.now)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.inv_foto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HFoto', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pedir_Deportes',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('pedir', models.PositiveSmallIntegerField()),
                ('Fecha_Solicitado', models.DateTimeField(default=django.utils.timezone.now)),
                ('Fecha_a_Pedir', models.DateField(default=django.utils.timezone.now)),
                ('Fecha_Limite', models.DateField(default=django.utils.timezone.now)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.inv_deportes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HDepo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pedir_Danzas',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('pedir', models.PositiveSmallIntegerField()),
                ('Fecha_Solicitado', models.DateTimeField(default=django.utils.timezone.now)),
                ('Fecha_a_Pedir', models.DateField(default=django.utils.timezone.now)),
                ('Fecha_Limite', models.DateField(default=django.utils.timezone.now)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.inv_danzas')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HDanzas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
