# Generated by Django 3.0.1 on 2019-12-29 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Name')),
                ('created_at', models.DateField(verbose_name='Created At')),
                ('modify_at', models.DateField(auto_now=True, verbose_name='Modify At')),
                ('category_id', models.ManyToManyField(to='products.Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['title'],
            },
        ),
    ]
