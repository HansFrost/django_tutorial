# Generated by Django 2.2.6 on 2019-10-10 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_auto_20191010_2132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='destination',
            new_name='name',
        ),
    ]
