# Generated by Django 4.2.1 on 2023-06-13 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_url_short_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='original_url',
            field=models.URLField(unique=True),
        ),
    ]
