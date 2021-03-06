# Generated by Django 4.0.2 on 2022-03-29 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='pet',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='pet',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='pet',
            unique_together={('user', 'name')},
        ),
        migrations.RemoveField(
            model_name='pet',
            name='user_profile',
        ),
    ]
