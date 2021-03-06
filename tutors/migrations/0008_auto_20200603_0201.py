# Generated by Django 3.0.6 on 2020-06-03 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutors', '0007_auto_20200603_0050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='nick',
        ),
        migrations.AddField(
            model_name='tutor',
            name='title',
            field=models.CharField(choices=[('mr', 'Mr.'), ('ms', 'Miss.'), ('mrs', 'Mrs.'), ('master', 'Master.'), ('dr', 'Dr.')], default='master', max_length=10),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='price',
            field=models.IntegerField(verbose_name='Price per Month'),
        ),
    ]
