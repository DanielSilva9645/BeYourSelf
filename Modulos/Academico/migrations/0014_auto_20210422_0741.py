# Generated by Django 3.1.4 on 2021-04-22 12:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0013_auto_20210420_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invmusica',
            name='Fecha_Solicitado',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]