# Generated by Django 3.0.2 on 2020-01-11 17:01

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
