# Generated by Django 3.1.4 on 2021-04-24 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0042_auto_20210424_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inv_musica',
            name='disponible',
            field=models.PositiveSmallIntegerField(default=''),
        ),
    ]
