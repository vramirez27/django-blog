# Generated by Django 3.0.8 on 2020-07-24 09:42

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0004_remove_article_illustration_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]
