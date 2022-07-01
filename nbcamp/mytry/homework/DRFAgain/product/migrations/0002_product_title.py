# Generated by Django 4.0.5 on 2022-06-27 06:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='제목'),
            preserve_default=False,
        ),
    ]
