# Generated by Django 4.1.5 on 2023-02-04 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('collage', models.CharField(max_length=200)),
                ('age', models.IntegerField(max_length=5)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
