# Generated by Django 4.1 on 2024-01-24 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chats',
            name='sender',
            field=models.CharField(max_length=200),
        ),
    ]
