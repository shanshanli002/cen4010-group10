# Generated by Django 3.2.12 on 2022-03-29 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_card_delete_creditcard'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Card',
        ),
        migrations.AddField(
            model_name='users',
            name='cc_number',
            field=models.CharField(default=1, max_length=13),
            preserve_default=False,
        ),
    ]
