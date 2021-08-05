# Generated by Django 2.2.5 on 2021-07-27 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('author', models.CharField(max_length=25)),
                ('published_year', models.CharField(max_length=4)),
                ('genre', models.CharField(max_length=10)),
                ('desc', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='images')),
            ],
        ),
    ]