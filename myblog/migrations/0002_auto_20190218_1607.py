# Generated by Django 2.1.4 on 2019-02-18 16:07

from django.db import migrations
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=django_summernote.fields.SummernoteTextField(verbose_name='内容'),
        ),
    ]