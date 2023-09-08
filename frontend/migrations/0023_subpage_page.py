# Generated by Django 4.2.1 on 2023-09-06 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0022_subpage_alter_post_page_post_sub_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='subpage',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_pages', to='frontend.page'),
        ),
    ]