# Generated by Django 3.2.18 on 2023-03-09 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0003_auto_20230309_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='subject',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]