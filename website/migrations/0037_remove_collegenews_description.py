# Generated by Django 4.1.7 on 2023-04-21 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0036_collegenews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collegenews',
            name='description',
        ),
    ]