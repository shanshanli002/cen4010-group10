# Generated by Django 4.0.2 on 2022-04-01 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_cardnumber_users_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='Number',
            new_name='number',
        ),
    ]
