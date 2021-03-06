# Generated by Django 3.0rc1 on 2019-12-05 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('review', models.TextField()),
                ('communication', models.IntegerField()),
                ('check_in', models.IntegerField()),
                ('accuracy', models.IntegerField()),
                ('value', models.IntegerField()),
                ('cleanliness', models.IntegerField()),
                ('location', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
