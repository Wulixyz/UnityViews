# Generated by Django 4.2.7 on 2023-11-06 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='yyd', max_length=20)),
                ('password', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
