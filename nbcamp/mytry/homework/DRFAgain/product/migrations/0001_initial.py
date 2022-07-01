# Generated by Django 4.0.5 on 2022-06-27 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(blank=True, upload_to='product/thumbnail/', verbose_name='썸네일')),
                ('desc', models.TextField(max_length=50, verbose_name='설명')),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='등록일자')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='수정일자')),
                ('exposure_start_date', models.DateTimeField(default=0, verbose_name='게시 시작 일자')),
                ('exposure_end_date', models.DateTimeField(default=0, verbose_name='게시 종료 일자')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성화 여부')),
                ('price', models.IntegerField(verbose_name='가격')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
    ]
