# Generated by Django 4.0 on 2022-01-03 02:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
