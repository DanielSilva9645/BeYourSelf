# Generated by Django 3.1.4 on 2021-05-22 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0060_auto_20210522_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedir_musica',
            name='pedir',
            field=models.CharField(default='', max_length=50),
        ),
    ]
