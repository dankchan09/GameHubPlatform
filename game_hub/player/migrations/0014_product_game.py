# Generated by Django 5.1.4 on 2025-01-28 15:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0013_game_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='player.game'),
        ),
    ]
