# Generated by Django 5.0.2 on 2024-02-10 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordgame', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchlist',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]