# Generated by Django 3.1.4 on 2021-06-13 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0036_auto_20210613_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='user_3.png', null=True, upload_to='perfiles/'),
        ),
    ]
