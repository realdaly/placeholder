# Generated by Django 4.2.1 on 2023-09-05 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0014_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]