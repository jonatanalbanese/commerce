# Generated by Django 3.2.8 on 2021-10-31 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comement_user',
            new_name='comment_user',
        ),
    ]
