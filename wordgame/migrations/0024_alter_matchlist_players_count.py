# Generated by Django 5.0.2 on 2024-02-29 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordgame', '0023_gamerslist_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchlist',
            name='players_count',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
