# Generated by Django 3.1.4 on 2021-04-24 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0036_auto_20210424_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedir_musica',
            name='pedir',
            field=models.PositiveSmallIntegerField(max_length=2),
        ),
    ]
