# Generated by Django 4.0.6 on 2022-07-15 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='post_images')),
                ('x', models.DecimalField(decimal_places=2, max_digits=5)),
                ('y', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cluster', models.IntegerField()),
            ],
        ),
    ]
