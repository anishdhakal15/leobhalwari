# Generated by Django 3.1.7 on 2021-04-07 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_background_background_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='leader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('post', models.CharField(default='', max_length=255)),
                ('image', models.ImageField(default='', upload_to='images')),
                ('year', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Background',
        ),
    ]
