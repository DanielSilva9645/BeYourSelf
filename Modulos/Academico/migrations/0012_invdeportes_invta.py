# Generated by Django 3.1.4 on 2021-04-18 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0011_auto_20210417_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvDeportes',
            fields=[
                ('codigo', models.CharField(default='', max_length=50)),
                ('materialess', models.CharField(default='', max_length=50, primary_key=True, serialize=False)),
                ('disponible', models.CharField(default='', max_length=2)),
                ('Fecha_Solicitado', models.DateField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='InvTA',
            fields=[
                ('codigo', models.CharField(default='', max_length=50)),
                ('materialess', models.CharField(default='', max_length=50, primary_key=True, serialize=False)),
                ('disponible', models.CharField(default='', max_length=2)),
                ('Fecha_Solicitado', models.DateField(default='')),
            ],
        ),
    ]
