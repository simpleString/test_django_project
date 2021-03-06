# Generated by Django 3.2.3 on 2021-05-29 18:20

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Title')),
                ('description', models.CharField(max_length=500, verbose_name='Description')),
                ('coordinate', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Place')),
                ('image', models.ImageField(upload_to='place_image', verbose_name='Place image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
