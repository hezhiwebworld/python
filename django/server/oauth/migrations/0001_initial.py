# Generated by Django 2.0 on 2018-06-20 09:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OAuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50, verbose_name='用户')),
                ('nickName', models.CharField(max_length=50, verbose_name='昵称')),
                ('openid', models.CharField(max_length=50, verbose_name='用户')),
                ('token', models.CharField(max_length=50, verbose_name='令牌')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间')),
            ],
        ),
    ]
