# Generated by Django 4.2.7 on 2024-02-01 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_customer_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='entry',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='notes',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]