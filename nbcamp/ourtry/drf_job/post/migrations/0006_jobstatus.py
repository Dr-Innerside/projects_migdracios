# Generated by Django 4.0.6 on 2022-07-22 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_jobpostactivity'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30, verbose_name='지원서 상태')),
            ],
            options={
                'db_table': 'job_status',
            },
        ),
    ]
