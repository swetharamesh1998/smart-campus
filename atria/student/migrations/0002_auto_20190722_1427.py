# Generated by Django 2.2.3 on 2019-07-22 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.AlterField(
            model_name='student',
            name='USN',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
