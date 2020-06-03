# Generated by Django 3.0.6 on 2020-06-03 00:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tutors', '0006_tutor_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='info',
            field=models.OneToOneField(default='09039049828', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tutor',
            name='phone_number',
            field=models.CharField(default='09039049828', max_length=11, verbose_name='Phone Number'),
            preserve_default=False,
        ),
    ]
