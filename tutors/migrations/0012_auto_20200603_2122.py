# Generated by Django 3.0.6 on 2020-06-03 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutors', '0011_tutor_date_joined'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutor',
            old_name='available',
            new_name='isAvailable',
        ),
        migrations.RenameField(
            model_name='tutor',
            old_name='verified',
            new_name='isVerified',
        ),
    ]