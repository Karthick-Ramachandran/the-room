# Generated by Django 2.1.4 on 2019-02-10 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0002_company_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='target_industries',
            field=models.ManyToManyField(blank=True, help_text='Top industries that you cater to. Add more industries if required using industry API', null=True, to='organisation.Industry'),
        ),
        migrations.AlterField(
            model_name='company',
            name='target_segments',
            field=models.ManyToManyField(blank=True, help_text='Choose the segments you cater to . Add more segments if required using Segment API', null=True, to='organisation.Segment'),
        ),
    ]
