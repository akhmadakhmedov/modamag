# Generated by Django 3.2.5 on 2021-08-08 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_alter_variation_variation_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('size', 'size'), ('color', 'color')], max_length=100),
        ),
    ]
