# Generated by Django 3.2.11 on 2022-01-12 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake_shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
        ),
    ]