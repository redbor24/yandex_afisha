# Generated by Django 4.0.6 on 2022-07-13 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_alter_place_description_long'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='Номер картинки на локации')),
                ('image', models.ImageField(null=True, upload_to='places', verbose_name='Картинка локации')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place', verbose_name='Локация')),
            ],
            options={
                'verbose_name': 'Изображение локации',
                'verbose_name_plural': 'Изображения локации',
            },
        ),
    ]