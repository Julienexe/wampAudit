# Generated by Django 3.2.8 on 2021-10-27 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_blogs', '0002_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default='Article', max_length=50),
        ),
    ]
