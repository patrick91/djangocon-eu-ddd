# Generated by Django 3.2.3 on 2021-05-25 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
            ],
        ),
    ]
