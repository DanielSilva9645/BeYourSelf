# Generated by Django 3.1.4 on 2021-04-22 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0004_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='avatar-mini4.jpg', upload_to=''),
        ),
    ]
