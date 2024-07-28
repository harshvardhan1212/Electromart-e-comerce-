# Generated by Django 4.2.1 on 2023-05-19 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_img_name_alter_img_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='product')),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.category1')),
            ],
        ),
        migrations.CreateModel(
            name='UserRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='entry',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='blog',
        ),
        migrations.DeleteModel(
            name='img',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]
