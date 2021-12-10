# Generated by Django 3.2.6 on 2021-09-29 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_name', models.CharField(max_length=100)),
                ('Event_category', models.CharField(default='', max_length=100)),
                ('Event_Desc', models.CharField(max_length=500)),
                ('Event_sponsor', models.CharField(default='', max_length=100)),
                ('Event_price', models.IntegerField(default=0)),
                ('Event_venue', models.CharField(default='', max_length=300)),
                ('Event_time', models.TimeField(default='')),
                ('Event_datetime', models.DateTimeField(default='')),
                ('Event_image', models.ImageField(default='', upload_to='media/event_img')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('News_title', models.CharField(max_length=200)),
                ('News_desc', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sponser_name', models.CharField(max_length=100)),
                ('Sponser_image', models.ImageField(default='', upload_to='media/sponser_img')),
                ('Sponser_desc', models.CharField(default='', max_length=300)),
            ],
        ),
    ]
