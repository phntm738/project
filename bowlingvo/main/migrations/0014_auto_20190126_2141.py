# Generated by Django 2.0.9 on 2019-01-26 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20190120_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='last_lang',
            field=models.IntegerField(default=0),
        ),
    ]
