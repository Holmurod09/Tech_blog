# Generated by Django 4.2 on 2023-05-18 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='media/')),
                ('faceboook', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('google', models.URLField(blank=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('date', models.CharField(max_length=100)),
                ('who', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='gadgets',
            name='images',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
