# Generated by Django 5.1 on 2024-08-15 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BRDLapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
