# Generated by Django 4.2.2 on 2023-06-15 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_alter_listing_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='band',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.band'),
        ),
    ]
