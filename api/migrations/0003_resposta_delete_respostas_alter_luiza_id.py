# Generated by Django 4.2.3 on 2023-07-20 19:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_respostas_alter_luiza_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reposta', models.TextField(max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Respostas',
        ),
        migrations.AlterField(
            model_name='luiza',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0f985377-8816-475b-a33e-96d12ea5eb0f'), primary_key=True, serialize=False),
        ),
    ]
