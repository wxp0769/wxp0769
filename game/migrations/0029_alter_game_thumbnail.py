# Generated by Django 4.2.9 on 2025-02-06 15:52

from django.db import migrations, models
import game.models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0028_alter_game_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='thumbnail',
            field=models.FileField(default='/uploads/default.png', upload_to=game.models.get_file_path, verbose_name='游戏图片'),
        ),
    ]
