# Generated by Django 3.0.7 on 2020-06-17 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200617_0739'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='subject',
            new_name='mentor',
        ),
    ]
