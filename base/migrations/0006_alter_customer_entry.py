# Generated by Django 4.2.7 on 2024-02-01 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_order_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='entry',
            field=models.CharField(default='', max_length=50),
        ),
    ]