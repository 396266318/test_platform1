# Generated by Django 3.1.3 on 2021-02-19 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='名称')),
                ('describe', models.TextField(default='', verbose_name='描述')),
                ('status', models.IntegerField(default=0, verbose_name='状态')),
                ('cases', models.TextField(default='', verbose_name='关联用例')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='名称')),
                ('errors', models.IntegerField(verbose_name='错误用例')),
                ('failures', models.IntegerField(verbose_name='失败用例')),
                ('skipped', models.IntegerField(verbose_name='跳过用例')),
                ('tests', models.IntegerField(verbose_name='总用例数')),
                ('run_time', models.FloatField(verbose_name='运行时长')),
                ('result', models.TextField(default='', verbose_name='详细')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_task.testtask')),
            ],
        ),
    ]
