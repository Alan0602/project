# Generated by Django 4.1.7 on 2023-04-15 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_cseevents_rename_newsimage_csenewsimage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CseEvents',
            new_name='CseEvent',
        ),
    ]
