# Generated by Django 3.1.7 on 2021-06-16 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventmaker', '0005_post_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.CharField(max_length=4000),
        ),
    ]
