# Generated by Django 4.0.2 on 2022-04-14 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '__first__'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customer')),
            ],
        ),
    ]
