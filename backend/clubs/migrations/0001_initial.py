# Generated by Django 5.0.3 on 2025-03-12 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('club_name', models.CharField(max_length=255)),
                ('club_description', models.TextField()),
                ('announcment', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
