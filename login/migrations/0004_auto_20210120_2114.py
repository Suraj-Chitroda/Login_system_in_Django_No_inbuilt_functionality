# Generated by Django 3.0.2 on 2021-01-20 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20210120_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login_user',
            name='birthdate',
        ),
        migrations.RemoveField(
            model_name='login_user',
            name='gender',
        ),
        migrations.AddField(
            model_name='login_user',
            name='password',
            field=models.CharField(default='null', max_length=254),
            preserve_default=False,
        ),
    ]