# Generated by Django 4.2.3 on 2023-07-27 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_like_kind'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='kind',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.kind'),
        ),
    ]
