# Generated by Django 5.0.2 on 2024-02-18 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordgame', '0018_gamerslist_queue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamerslist',
            name='queue',
            field=models.IntegerField(default=0),
        ),
    ]
