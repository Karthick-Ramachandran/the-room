# Generated by Django 2.1.4 on 2019-02-06 15:38

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the Company', max_length=255)),
                ('domain', models.CharField(help_text='Domain of the Company', max_length=255)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(help_text='Phone Number in E164 format which includes the country code also. eg : +91984765854', max_length=128)),
                ('head_quaters', models.CharField(max_length=255)),
                ('region_of_operation', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=70, unique=True)),
                ('address', models.TextField(help_text='Address of the Company.')),
                ('number_of_paid_customers', models.PositiveIntegerField(default=0)),
                ('number_of_free_customers', models.PositiveIntegerField(default=0)),
                ('funding', models.CharField(choices=[('public', 'Public Funding'), ('private', 'Private Funding'), ('no', 'No')], max_length=10)),
                ('deployment_size', models.PositiveIntegerField(default=0, help_text='Deployment size in integer')),
                ('pitch_deck_file', models.FileField(blank=True, null=True, upload_to='pitch_decks/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hyperlink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hyperlinks', to='organisation.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='target_industries',
            field=models.ManyToManyField(help_text='Top industries that you cater to. Add more industries if required using industry API', to='organisation.Industry'),
        ),
        migrations.AddField(
            model_name='company',
            name='target_segments',
            field=models.ManyToManyField(help_text='Choose the segments you cater to . Add more segments if required using Segment API', to='organisation.Segment'),
        ),
    ]
