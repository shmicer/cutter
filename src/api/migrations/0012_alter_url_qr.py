# Generated by Django 4.2.2 on 2023-06-27 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_url_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='qr',
            field=models.ImageField(null=True, upload_to='static/images'),
        ),
    ]
