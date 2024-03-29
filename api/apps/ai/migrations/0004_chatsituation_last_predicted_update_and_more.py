# Generated by Django 4.2.6 on 2023-10-28 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0003_alter_chatsituation_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatsituation',
            name='last_predicted_update',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='chatsituation',
            name='predicted_emotions',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
