# Generated by Django 3.2 on 2021-04-14 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='balcony',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bedrooms',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='garage',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='listing',
            name='hall',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='listing',
            name='kitchen',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_1',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='sqft',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='zipcode',
            field=models.BigIntegerField(),
        ),
    ]
