# Generated by Django 3.1.3 on 2021-02-18 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_manage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('url', models.TextField(verbose_name='URL')),
                ('method', models.IntegerField(verbose_name='请求方法')),
                ('header', models.TextField(verbose_name='请求头')),
                ('parameter_type', models.IntegerField(verbose_name='参数类型')),
                ('parameter_body', models.TextField(verbose_name='参数内容')),
                ('result', models.TextField(verbose_name='结果')),
                ('assert_type', models.IntegerField(verbose_name='断言类型')),
                ('assert_text', models.TextField(verbose_name='断言结果')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_manage.module')),
            ],
        ),
    ]
