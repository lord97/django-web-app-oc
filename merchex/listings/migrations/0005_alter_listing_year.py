# Generated by Django 4.2.2 on 2023-06-15 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_listing_description_listing_sold_listing_types_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]