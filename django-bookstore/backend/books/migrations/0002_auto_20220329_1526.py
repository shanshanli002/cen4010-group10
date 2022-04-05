# Generated by Django 3.2.12 on 2022-03-29 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=200)),
                ('Last_Name', models.CharField(max_length=200)),
                ('Bio', models.CharField(max_length=10000)),
                ('Publisher', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Edition',
            new_name='Copies_Sold',
        ),
        migrations.RemoveField(
            model_name='book',
            name='title',
        ),
        migrations.AddField(
            model_name='book',
            name='Book_Description',
            field=models.CharField(default=100, max_length=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='Genre',
            field=models.CharField(default=100, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='ISBN',
            field=models.IntegerField(default=123456789),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='Publisher',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='Title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='Year_Published',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='Author',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='Price',
            field=models.FloatField(),
        ),
    ]