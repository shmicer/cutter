# Generated by Django 4.2.2 on 2023-06-27 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_url_short_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='qr',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]