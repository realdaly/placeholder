# Generated by Django 4.2.1 on 2023-08-12 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Social_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('link', models.CharField(blank=True, max_length=1000, null=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='frontend.image')),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
