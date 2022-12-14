# Generated by Django 4.1.1 on 2022-09-21 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Holding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('isin', models.CharField(max_length=50)),
                ('current_price', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('asset_group', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'holdings',
            },
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('principal', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'investments',
            },
        ),
        migrations.CreateModel(
            name='HoldingsRegist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature', models.CharField(default='', max_length=300)),
                ('transfer_identifier', models.IntegerField(default=0)),
                ('holding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.holding')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'holdings_regist',
            },
        ),
        migrations.CreateModel(
            name='FinalHolding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('holding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.holding')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'final_holdings',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=100)),
                ('account_number', models.IntegerField()),
                ('total_assests', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
    ]
