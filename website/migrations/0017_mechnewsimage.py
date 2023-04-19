# Generated by Django 4.1.7 on 2023-04-18 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_mechnews'),
    ]

    operations = [
        migrations.CreateModel(
            name='MechNewsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=300)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('mechDepartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='website.mechnews')),
            ],
        ),
    ]
