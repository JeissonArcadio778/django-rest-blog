# Generated by Django 4.2 on 2023-04-10 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='web_site',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
