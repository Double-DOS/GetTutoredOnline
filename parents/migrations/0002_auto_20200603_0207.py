# Generated by Django 3.0.6 on 2020-06-03 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorrequest',
            name='requested_duration',
            field=models.PositiveIntegerField(verbose_name='Months_Needed'),
        ),
    ]
