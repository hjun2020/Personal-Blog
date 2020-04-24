# Generated by Django 3.0.5 on 2020-04-22 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200422_0122'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='title',
            field=models.CharField(default='NO CONTENT', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='posting',
            name='text',
            field=models.TextField(default='NO CONTENT'),
        ),
    ]