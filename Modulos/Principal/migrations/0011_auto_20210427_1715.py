# Generated by Django 3.1.4 on 2021-04-27 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0010_auto_20210427_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
