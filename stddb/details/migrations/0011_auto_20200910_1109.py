# Generated by Django 3.1.1 on 2020-09-10 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0010_auto_20200910_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
