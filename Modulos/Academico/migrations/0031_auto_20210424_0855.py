# Generated by Django 3.1.4 on 2021-04-24 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0030_auto_20210424_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inv_foto',
            name='codigo',
            field=models.AutoField(default='', primary_key=True, serialize=False),
        ),
    ]
