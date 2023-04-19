# Generated by Django 4.1.7 on 2023-04-19 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0023_mechevent_alter_cseevent_google_form_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MechTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('profile_picture', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=100)),
                ('qualification', models.TextField(max_length=200)),
                ('role', models.CharField(max_length=100)),
                ('experience', models.TextField(max_length=400)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
