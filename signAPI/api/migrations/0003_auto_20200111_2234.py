# Generated by Django 3.0.2 on 2020-01-11 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='Phone',
            field=models.CharField(max_length=20),
        ),
    ]
