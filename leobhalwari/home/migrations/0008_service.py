# Generated by Django 3.1.7 on 2021-04-07 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_bod_committee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('string', models.CharField(default='', max_length=10000)),
                ('image', models.ImageField(default='', upload_to='images')),
            ],
        ),
    ]
