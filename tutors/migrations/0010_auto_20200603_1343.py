# Generated by Django 3.0.6 on 2020-06-03 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutors', '0009_tutor_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='medium',
            field=models.CharField(choices=[('online', 'Online Tutoring'), ('physical', 'Physical Tutoring'), ('both', 'Both')], default='online', max_length=10),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='gender',
            field=models.CharField(choices=[('m', 'Male'), ('fm', 'Female')], default='m', max_length=6),
        ),
    ]
