# Generated by Django 5.1.1 on 2024-09-26 10:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_conversion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='video_conversion.video'),
        ),
    ]
