# Generated by Django 2.1.1 on 2019-03-06 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('medicine', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
