# Generated by Django 5.0.2 on 2024-02-29 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_rename_seller_id_landing_book_seller_id_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landing_book',
            name='COVER_PAGE',
            field=models.BinaryField(),
        ),
    ]