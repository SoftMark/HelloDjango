# Generated by Django 3.1.3 on 2021-01-10 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings_content', '0004_auto_20210110_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chihuahua',
            name='gender',
            field=models.CharField(choices=[('a', 'сука'), ('b', 'кобель')], default='a', max_length=20, verbose_name='Пол'),
        ),
    ]