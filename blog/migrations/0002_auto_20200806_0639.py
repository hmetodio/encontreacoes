# Generated by Django 2.2.14 on 2020-08-06 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publishied_date',
            new_name='published_date',
        ),
    ]
