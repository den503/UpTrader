# Generated by Django 3.0.3 on 2020-02-18 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20200218_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='child',
        ),
        migrations.AddField(
            model_name='item',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child', to='menu.Item'),
        ),
    ]
