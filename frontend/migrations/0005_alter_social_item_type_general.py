# Generated by Django 4.2.1 on 2023-08-14 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_remove_social_item_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social_item',
            name='type',
            field=models.CharField(blank=True, choices=[('facebook', 'facebook'), ('instagram', 'instagram'), ('telegram', 'telegram'), ('twitter', 'twitter'), ('whatsapp', 'whatsapp'), ('youtube', 'youtube')], max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='logo', to='frontend.image')),
            ],
        ),
    ]
