# Generated by Django 2.1.3 on 2019-02-23 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cook', '0005_auto_20190224_0033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='recipie',
            old_name='name',
            new_name='title',
        ),
    ]
