# Generated by Django 2.2.6 on 2019-10-17 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('madplan', '0007_auto_20191017_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipestep',
            name='recipe',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='madplan.Recipe'),
        ),
    ]
