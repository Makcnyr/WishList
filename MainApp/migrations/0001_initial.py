# Generated by Django 2.1.2 on 2018-10-29 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=120, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('url', models.URLField()),
                ('post', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
    ]
