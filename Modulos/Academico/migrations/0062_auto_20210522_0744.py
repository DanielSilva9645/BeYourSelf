# Generated by Django 3.1.4 on 2021-05-22 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0061_auto_20210522_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedir_musica',
            name='pedir',
            field=models.IntegerField(),
        ),
    ]
