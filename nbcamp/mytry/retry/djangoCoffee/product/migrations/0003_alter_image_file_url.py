# Generated by Django 4.0.5 on 2022-06-05 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_image_file_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file_url',
            field=models.URLField(max_length=500),
        ),
    ]
