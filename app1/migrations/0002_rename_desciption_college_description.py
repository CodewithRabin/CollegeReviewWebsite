# Generated by Django 4.1 on 2022-08-25 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='college',
            old_name='desciption',
            new_name='description',
        ),
    ]
