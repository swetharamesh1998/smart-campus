# Generated by Django 2.2.3 on 2019-07-23 10:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20190722_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=10)),
                ('passcode', models.CharField(max_length=8, validators=[django.core.validators.MinLengthValidator(8)])),
            ],
        ),
    ]
