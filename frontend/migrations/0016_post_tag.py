# Generated by Django 4.2.1 on 2023-09-05 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0015_post_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.CharField(choices=[('news', 'خبر'), ('activity', 'نشاط')], default='news', max_length=20),
        ),
    ]
