# Generated by Django 2.2.6 on 2019-10-17 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madplan', '0002_macronutrients_energy_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipedescription',
            name='recipe_headline',
            field=models.CharField(max_length=50),
        ),
    ]
