# Generated by Django 4.1.7 on 2023-03-16 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ecommerce_store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('ecommerce_store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='ecommerce_store.ecommercestore')),
            ],
        ),
    ]
