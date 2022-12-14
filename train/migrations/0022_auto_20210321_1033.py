# Generated by Django 4.1 on 2021-03-21 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0021_auto_20210314_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routine',
            name='client',
            field=models.ForeignKey(limit_choices_to={'is_staff': 'False'}, on_delete=django.db.models.deletion.CASCADE, related_name='routines', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='routine',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Routine Name'),
        ),
    ]
