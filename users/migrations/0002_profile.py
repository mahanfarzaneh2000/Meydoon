<<<<<<< Updated upstream
# Generated by Django 3.1.7 on 2021-04-09 14:37

from django.conf import settings
=======
# Generated by Django 3.1.7 on 2021-04-08 23:08

>>>>>>> Stashed changes
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
<<<<<<< Updated upstream
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(default='default.jpg', upload_to='pics')),
                ('id_number', models.CharField(blank=True, max_length=50, null=True)),
                ('degree', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=400, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
=======
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
                ('profile_pic', models.ImageField(upload_to='')),
                ('card_number', models.CharField(blank=True, max_length=50, null=True)),
                ('degree', models.CharField(blank=True, max_length=20, null=True)),
                ('gig', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
>>>>>>> Stashed changes
            ],
        ),
    ]
