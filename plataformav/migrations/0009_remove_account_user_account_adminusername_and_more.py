# Generated by Django 5.0.3 on 2024-11-26 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataformav', '0008_alter_account_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
        migrations.AddField(
            model_name='account',
            name='adminUsername',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Nome de Usuário Admin'),
        ),
        migrations.AddField(
            model_name='account',
            name='password',
            field=models.CharField(default=123456, max_length=128, verbose_name='Senha do Superusuário'),
            preserve_default=False,
        ),
    ]
