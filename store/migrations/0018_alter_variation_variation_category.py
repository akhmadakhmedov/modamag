# Generated by Django 3.2.5 on 2021-08-08 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_alter_variation_variation_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('size', 'размер'), ('color', 'color')], max_length=100),
        ),
    ]
