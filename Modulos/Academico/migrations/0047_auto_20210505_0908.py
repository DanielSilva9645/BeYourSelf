# Generated by Django 3.1.4 on 2021-05-05 14:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0046_auto_20210424_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedir_musica',
            name='Fecha_a_Pedir',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='pedir_musica',
            name='Fecha_Solicitado',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
