# Generated by Django 4.1.2 on 2022-12-07 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinorder',
            name='is_active',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='nmb',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='price_per_item',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]