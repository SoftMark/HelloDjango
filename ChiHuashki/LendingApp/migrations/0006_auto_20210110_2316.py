# Generated by Django 3.1.3 on 2021-01-10 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings_content', '0005_auto_20210110_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chihuahua',
            name='gender',
            field=models.CharField(choices=[('suka', 'сука'), ('kobel', 'кобель')], default='suka', max_length=20, verbose_name='Пол'),
        ),
    ]