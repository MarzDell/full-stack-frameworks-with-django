# Generated by Django 2.2 on 2020-04-29 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='brand',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='model_type',
        ),
    ]
