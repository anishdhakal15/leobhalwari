# Generated by Django 3.1.7 on 2021-04-07 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210407_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='BOD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('post', models.CharField(default='', max_length=255)),
                ('image', models.ImageField(default='', upload_to='images')),
                ('facebook_link', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('post', models.CharField(default='', max_length=255)),
                ('image', models.ImageField(default='', upload_to='images')),
                ('facebook_link', models.CharField(default='', max_length=255)),
            ],
        ),
    ]