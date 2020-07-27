# Generated by Django 3.0.8 on 2020-07-27 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_isstudent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='isStudent',
        ),
        migrations.AddField(
            model_name='customuser',
            name='usertype',
            field=models.CharField(blank=True, max_length=600),
        ),
    ]