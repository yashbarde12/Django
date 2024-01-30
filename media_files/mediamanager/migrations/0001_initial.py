# Generated by Django 5.0 on 2024-01-30 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('Audio', 'Audio'), ('Video', 'Video'), ('Image', 'Image')], max_length=10)),
                ('format', models.CharField(max_length=10)),
                ('size', models.IntegerField()),
                ('duration_secs', models.IntegerField(default=0)),
            ],
        ),
    ]
