# Generated by Django 4.0.2 on 2022-02-16 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_pet'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('tagged_pets', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('date_of_publication', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='user_profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.profile'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='pet',
            unique_together={('user_profile', 'name')},
        ),
    ]
