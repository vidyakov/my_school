# Generated by Django 3.0.8 on 2020-07-16 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(blank=True, max_length=512, unique=True, verbose_name='название'),
        ),
    ]
