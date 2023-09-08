# Generated by Django 4.2.1 on 2023-09-06 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0018_page_is_nav_alter_main_slider_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='more_info',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.CharField(blank=True, choices=[('news', 'خبر'), ('activity', 'نشاط')], default='news', max_length=20, null=True),
        ),
    ]