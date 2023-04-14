# Generated by Django 3.2 on 2023-04-13 14:31

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_subscriptions_users_subscriptions_prevent_self_subscription'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='subscriptions',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, author=django.db.models.expressions.F('user')), name='users_subscriptions_prevent_self_subscription'),
        ),
    ]