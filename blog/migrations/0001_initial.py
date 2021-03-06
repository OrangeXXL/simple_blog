# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('author', models.CharField(max_length=16, verbose_name='作者')),
                ('content', models.TextField(verbose_name='正文')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='名称')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='称呼')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('content', models.CharField(max_length=140, verbose_name='内容')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('blog', models.ForeignKey(verbose_name='博客', to='blog.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='名称')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(verbose_name='分类', to='blog.Category'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='标签'),
        ),
    ]
