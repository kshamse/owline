# Generated by Django 3.2.18 on 2023-03-04 09:07

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_alter_basepost_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title'),
        ),
    ]
