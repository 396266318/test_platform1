# Generated by Django 3.1.3 on 2021-02-18 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100, verbose_name='名称')),
                ('value', models.CharField(max_length=500, verbose_name='值')),
                ('describe', models.TextField(default='', verbose_name='描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
        ),
    ]
