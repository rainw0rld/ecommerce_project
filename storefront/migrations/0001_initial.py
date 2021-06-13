# Generated by Django 3.2.3 on 2021-06-11 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
                ('viewcount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ProductAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='media/img/album_img')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album', to='storefront.productdetail')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('thumbnail', models.ImageField(null=True, upload_to='media/img/title_img/')),
                ('brand', models.ForeignKey(default='UNKNOWN', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='storefront.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='storefront.category')),
            ],
        ),
    ]
