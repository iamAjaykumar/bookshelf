# Generated by Django 2.2.5 on 2021-07-28 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210728_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinformation',
            name='title',
            field=models.CharField(max_length=28),
        ),
    ]
