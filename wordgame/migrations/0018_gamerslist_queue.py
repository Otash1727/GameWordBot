# Generated by Django 5.0.2 on 2024-02-18 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordgame', '0017_gamerslist_chance'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamerslist',
            name='queue',
            field=models.IntegerField(default=1),
        ),
    ]