# Generated by Django 4.1.7 on 2023-04-19 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0027_merge_0026_civilnewsimage_0026_eeenews'),
    ]

    operations = [
        migrations.CreateModel(
            name='CivilEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('poster', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=300)),
                ('last_date', models.CharField(max_length=50)),
                ('google_form', models.CharField(blank=True, max_length=300, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]
