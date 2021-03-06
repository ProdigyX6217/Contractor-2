# Generated by Django 3.0.2 on 2020-03-05 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('website', models.URLField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('upload', models.ImageField(height_field=300, upload_to='business_photos/', width_field=300)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('business_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='yelp.Business')),
            ],
            bases=('yelp.business',),
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('business_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='yelp.Business')),
            ],
            bases=('yelp.business',),
        ),
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('business_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='yelp.Business')),
            ],
            bases=('yelp.business',),
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('business_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='yelp.Business')),
            ],
            bases=('yelp.business',),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('business_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='yelp.Business')),
            ],
            bases=('yelp.business',),
        ),
    ]
