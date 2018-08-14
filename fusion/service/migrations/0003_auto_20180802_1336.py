# Generated by Django 2.0.1 on 2018-08-02 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20180720_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='link',
            unique_together={('partner', 'url')},
        ),
    ]