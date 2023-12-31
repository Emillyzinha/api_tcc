# Generated by Django 4.2.4 on 2023-08-21 12:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_alter_palavras_id_palavras_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='id_usuario',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='senha',
            field=models.TextField(default=uuid.uuid4, max_length=100),
        ),
    ]
