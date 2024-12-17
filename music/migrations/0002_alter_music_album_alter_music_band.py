# Generated by Django 5.1.1 on 2024-09-27 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
        ('performer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tracks', to='music.album'),
        ),
        migrations.AlterField(
            model_name='music',
            name='band',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='performer.band'),
        ),
    ]
