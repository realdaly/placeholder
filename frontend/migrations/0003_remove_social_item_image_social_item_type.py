# Generated by Django 4.2.1 on 2023-08-13 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_image_social_item_delete_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='social_item',
            name='image',
        ),
        migrations.AddField(
            model_name='social_item',
            name='type',
            field=models.CharField(blank=True, choices=[('facebook', 'facebook'), ('instagram', 'instagram'), ('telegram', 'telegram'), ('twiiter', 'twiiter'), ('whatsapp', 'whatsapp'), ('youtube', 'youtube')], max_length=20, null=True),
        ),
    ]