# Generated by Django 4.1.4 on 2023-01-19 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proger', '0003_remove_post_author_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='URL'),
        ),
    ]
