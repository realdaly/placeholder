# Generated by Django 4.2.1 on 2023-08-31 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0008_main_slider_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_slider',
            name='body',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='main_slider',
            name='title',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
    ]
