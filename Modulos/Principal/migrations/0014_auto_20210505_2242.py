# Generated by Django 3.1.4 on 2021-05-06 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0013_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='user_3.png', upload_to=''),
        ),
    ]
