# Generated by Django 5.1.5 on 2025-02-05 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='desc',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='post',
            name='tittle',
            field=models.CharField(max_length=200),
        ),
    ]
