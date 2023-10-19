# Generated by Django 3.1.4 on 2021-04-24 17:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Academico', '0038_auto_20210424_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inv_deportes',
            name='Fecha_Limite',
        ),
        migrations.RemoveField(
            model_name='inv_deportes',
            name='Fecha_Solicitado',
        ),
        migrations.RemoveField(
            model_name='inv_deportes',
            name='user',
        ),
        migrations.CreateModel(
            name='Pedir_Deportes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedir', models.PositiveSmallIntegerField()),
                ('Fecha_Solicitado', models.DateField(default=django.utils.timezone.now)),
                ('Fecha_Limite', models.DateField()),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.inv_deportes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='in_Depo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]