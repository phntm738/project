# Generated by Django 2.1.2 on 2018-12-19 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20181219_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='url_name',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
