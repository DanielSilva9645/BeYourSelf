# Generated by Django 3.1.4 on 2021-04-21 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0012_invdeportes_invta'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvDanzas',
            fields=[
                ('codigo', models.CharField(default='', max_length=50)),
                ('materialess', models.CharField(default='', max_length=50, primary_key=True, serialize=False)),
                ('disponible', models.CharField(default='', max_length=5)),
                ('Fecha_Solicitado', models.DateField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='InvFoto',
            fields=[
                ('codigo', models.CharField(default='', max_length=50)),
                ('materialess', models.CharField(default='', max_length=50, primary_key=True, serialize=False)),
                ('disponible', models.CharField(default='', max_length=5)),
                ('Fecha_Solicitado', models.DateField(default='')),
            ],
        ),
        migrations.AlterField(
            model_name='invdeportes',
            name='disponible',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='invmusica',
            name='disponible',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='invpintura',
            name='disponible',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='invta',
            name='disponible',
            field=models.CharField(default='', max_length=5),
        ),
    ]
