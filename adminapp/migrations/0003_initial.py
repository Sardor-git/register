# Generated by Django 4.2.4 on 2023-09-03 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminapp', '0002_remove_group_faculty_remove_student_group_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
