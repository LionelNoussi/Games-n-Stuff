# Generated by Django 3.1.4 on 2020-12-30 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0003_students'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Students',
            new_name='Student',
        ),
    ]
