# Generated by Django 2.1.8 on 2019-05-23 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=200)),
                ('featured_image', models.ImageField(max_length=255, upload_to='images/products/%Y/%m/', verbose_name='Featured Image')),
                ('post_date', models.DateTimeField(verbose_name='date published')),
                ('author', models.CharField(max_length=200)),
                ('excerpt', models.CharField(max_length=200)),
                ('category', models.ManyToManyField(to='blog.Category')),
            ],
        ),
    ]