# Generated by Django 4.2 on 2023-04-04 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('stone', 'Камень'), ('scissors', 'Ножницы'), ('paper', 'Бумага')], max_length=10)),
            ],
        ),
    ]
