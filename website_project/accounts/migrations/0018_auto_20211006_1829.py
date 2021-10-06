# Generated by Django 3.2.7 on 2021-10-06 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_userprofile_profileimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(blank=True, choices=[('M', 'Member'), ('BM', 'Board Member'), ('F', 'Faculty')], default='M', max_length=15, null=True),
        ),
    ]
