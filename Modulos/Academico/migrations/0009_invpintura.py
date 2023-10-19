# Generated by Django 3.1.7 on 2021-03-25 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0008_auto_20210324_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvPintura',
            fields=[
                ('materialess', models.CharField(choices=[('Pincel', 'Pincel'), ('Pintura Roja', 'Pintura Roja'), ('Pintura Azul', 'Pintura Azul'), ('Cuadro de Lienzo', 'Cuadro de Lienzo')], default='', max_length=50, primary_key=True, serialize=False)),
                ('disponible', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], default='', max_length=2)),
                ('Fecha', models.DateField(default='')),
            ],
        ),
    ]