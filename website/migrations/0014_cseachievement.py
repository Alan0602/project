# Generated by Django 4.1.7 on 2023-04-17 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_alter_cseteacher_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='CseAchievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=500)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]
