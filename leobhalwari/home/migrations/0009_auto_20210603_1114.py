# Generated by Django 3.1.7 on 2021-06-03 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_service'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Committee',
            new_name='Team',
        ),
        migrations.DeleteModel(
            name='BOD',
        ),
    ]
