# Generated by Django 3.1.4 on 2021-05-12 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0015_auto_20210512_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Usuario',
            field=models.CharField(default='', max_length=100),
        ),
    ]