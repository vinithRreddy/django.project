# Generated by Django 3.1.1 on 2020-09-10 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0007_auto_20200910_1103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faculty',
            old_name='name',
            new_name='Faculty_name',
        ),
    ]
