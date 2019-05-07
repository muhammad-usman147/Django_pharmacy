# Generated by Django 2.1.1 on 2019-03-11 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('stk_dtl', models.ForeignKey(on_delete='CASCADE', to='stocks.Stocks_Details')),
            ],
        ),
    ]
