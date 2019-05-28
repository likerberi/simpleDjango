# Generated by Django 2.2.1 on 2019-05-27 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fly', '0002_fly'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flys', models.ManyToManyField(blank=True, related_name='passengers', to='fly.Fly')),
            ],
        ),
    ]