# Generated by Django 5.0.2 on 2024-02-13 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordgame', '0009_englishdictionary'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EnglishDictionary',
        ),
    ]