# Generated by Django 4.0.3 on 2022-04-05 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_Name', models.CharField(blank=True, max_length=254)),
                ('Last_Name', models.CharField(blank=True, max_length=254)),
                ('Email_id', models.EmailField(blank=True, max_length=254)),
                ('Mobile_Number', models.CharField(blank=True, max_length=254)),
                ('Password', models.CharField(blank=True, max_length=254)),
            ],
        ),
    ]
