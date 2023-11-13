# Generated by Django 4.2.4 on 2023-09-19 17:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_alter_usuario_id_usuario_alter_usuario_senha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treinamentos',
            fields=[
                ('id_curso', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=255)),
                ('imagem', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.DeleteModel(
            name='Treinamento1',
        ),
    ]
