# Generated by Django 4.1.7 on 2023-03-16 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_product_cost_alter_product_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch_one',
            name='classification',
            field=models.CharField(default='その他', max_length=10, verbose_name='分類'),
        ),
        migrations.AddField(
            model_name='branch_three',
            name='classification',
            field=models.CharField(default='その他', max_length=10, verbose_name='分類'),
        ),
        migrations.AddField(
            model_name='branch_two',
            name='classification',
            field=models.CharField(default='その他', max_length=10, verbose_name='分類'),
        ),
        migrations.AddField(
            model_name='central_product',
            name='classification',
            field=models.CharField(default='その他', max_length=10, verbose_name='分類'),
        ),
        migrations.AddField(
            model_name='product',
            name='classification',
            field=models.CharField(choices=[['野菜', '野菜'], ['肉類', '肉類'], ['フルーツ', 'フルーツ'], ['調味料', '調味料'], ['その他', 'その他']], default='その他', max_length=10, verbose_name='分類'),
        ),
    ]
