# Generated by Django 3.0 on 2019-12-16 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AboutUs', '0002_auto_20191216_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='img',
            field=models.ImageField(default='AboutUsimgs/default.png', upload_to='AboutUsimgs/'),
        ),
    ]