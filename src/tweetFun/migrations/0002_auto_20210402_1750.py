# Generated by Django 3.1 on 2021-04-03 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetFun', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-id']},
        ),
    ]