# Generated by Django 3.1.2 on 2020-10-16 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0002_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]