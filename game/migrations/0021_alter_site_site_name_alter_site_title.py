# Generated by Django 4.2.9 on 2025-02-02 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0020_alter_site_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='site_name',
            field=models.CharField(max_length=128, verbose_name='站点名称'),
        ),
        migrations.AlterField(
            model_name='site',
            name='title',
            field=models.CharField(max_length=128, verbose_name='SEO标题'),
        ),
    ]
