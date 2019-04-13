# Generated by Django 2.2 on 2019-04-11 21:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('main', '0008_theorytask'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrameRecord',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('max_frames', models.IntegerField()),
                ('cur_frame', models.IntegerField(default=0)),
                ('score_table', models.TextField(blank=True, null=True)),
                ('frame_score', models.IntegerField(default=0)),
            ],
        ),
    ]
