# Generated by Django 2.0.1 on 2018-08-14 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20180814_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256, null=True)),
                ('is_completed', models.IntegerField()),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='service.Partner')),
            ],
        ),
    ]