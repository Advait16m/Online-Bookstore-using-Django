# Generated by Django 4.2.4 on 2023-10-04 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0003_book_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='totalrating',
            field=models.FloatField(default=0.0),
        ),
    ]
