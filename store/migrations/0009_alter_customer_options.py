# Generated by Django 4.1.7 on 2023-02-28 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_order_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['user__first_name', 'user__last_name'], 'permissions': [('view_history', 'Can view history')]},
        ),
    ]
