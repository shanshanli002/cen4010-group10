# Generated by Django 4.0.2 on 2022-04-09 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookRating', '0003_alter_comment_author_alter_comment_book'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together=set(),
        ),
    ]