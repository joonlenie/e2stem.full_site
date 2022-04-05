# Generated by Django 4.0 on 2022-04-05 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_blogpost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='text',
            new_name='text_en',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='title',
            new_name='title_en',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='text_kh',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='title_kh',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
