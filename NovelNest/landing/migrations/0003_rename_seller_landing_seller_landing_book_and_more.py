# Generated by Django 5.0.2 on 2024-02-29 07:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_rename_bname_book_bname_rename_b_id_book_b_id_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Seller',
            new_name='landing_seller',
        ),
        migrations.CreateModel(
            name='landing_book',
            fields=[
                ('B_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('BNAME', models.CharField(max_length=30)),
                ('PRICE', models.IntegerField()),
                ('COVER_PAGE', models.BinaryField(max_length=1000000)),
                ('SELLER_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.landing_seller')),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
