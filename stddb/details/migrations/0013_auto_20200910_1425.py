# Generated by Django 3.1.1 on 2020-09-10 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0012_auto_20200910_1118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faculty',
            old_name='Facultyname',
            new_name='Faculty_name',
        ),
    ]
