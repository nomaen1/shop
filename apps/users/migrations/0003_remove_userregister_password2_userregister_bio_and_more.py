# Generated by Django 4.2.2 on 2023-06-29 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_userregister_lll_userregister_password2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userregister',
            name='password2',
        ),
        migrations.AddField(
            model_name='userregister',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='БИО'),
        ),
        migrations.AlterField(
            model_name='userregister',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]