# Generated by Django 3.1.3 on 2021-02-01 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings_content', '0004_auto_20210129_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfigurations',
            name='footer_title',
            field=models.CharField(default='Заголовок футера', max_length=30, verbose_name='Заголовок'),
        ),
    ]
