# Generated by Django 3.1.4 on 2021-03-25 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0005_studentlogin'),
    ]

    operations = [
        migrations.CreateModel(
            name='CamposArts',
            fields=[
                ('camposss', models.CharField(choices=[('Fo', 'Fotografia'), ('D', 'Danzas'), ('Fu', 'Futbol'), ('B', 'Basquetboll'), ('M', 'Musica'), ('E', 'Expresion Corporal'), ('P', 'Pintura')], default='', max_length=2, primary_key=True, serialize=False)),
            ],
        ),
    ]
