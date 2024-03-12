# Generated by Django 5.0 on 2024-03-12 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('Snacks', 'Snacks'), ('Beverages', 'Beverages'), ('Sweets', 'Sweets')], max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='menu_images/')),
            ],
        ),
    ]
