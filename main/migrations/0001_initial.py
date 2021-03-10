# Generated by Django 3.1.5 on 2021-03-10 04:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Q', models.TextField()),
                ('A', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Feedbacks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.CharField(max_length=1000)),
                ('Message', models.TextField()),
                ('Date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Logos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Logo', models.ImageField(upload_to='logo')),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MessageBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=2000)),
                ('MessagePartner', models.CharField(max_length=2000)),
                ('UnreadMessages', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SendBy', models.CharField(max_length=2000)),
                ('Message', models.TextField()),
                ('RecievedBy', models.CharField(max_length=2000)),
                ('DateTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=900)),
                ('Message', models.TextField()),
                ('Date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServicesCatagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=300)),
                ('Image', models.ImageField(upload_to='catagoryImages')),
                ('Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.images')),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rating', models.FloatField(default=3)),
                ('MainImage', models.ImageField(upload_to='serviceMainImages')),
                ('ShopName', models.CharField(max_length=3000)),
                ('PriceType', models.CharField(max_length=300)),
                ('OpenTime', models.CharField(max_length=300)),
                ('closeTime', models.CharField(max_length=300)),
                ('Description', models.TextField(default='Description box is empty.')),
                ('VStatus', models.BooleanField(default=False)),
                ('RatedBy', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('SearchNames', models.ManyToManyField(blank=True, to='main.SearchName')),
                ('ServiceFeedback', models.ManyToManyField(blank=True, to='main.ServiceFeedback')),
                ('ServiceImages', models.ManyToManyField(blank=True, to='main.Images')),
                ('Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.servicescatagory')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.TextField()),
                ('MobileNo', models.CharField(max_length=20)),
                ('Image', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.images')),
                ('Service', models.ManyToManyField(blank=True, to='main.Service')),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PlanName', models.CharField(max_length=900)),
                ('Description', models.TextField()),
                ('Rate', models.CharField(max_length=500)),
                ('Open', models.BooleanField(default=False)),
                ('PlanServices', models.ManyToManyField(blank=True, to='main.Service')),
            ],
        ),
        migrations.CreateModel(
            name='InterestedService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Services', models.ManyToManyField(blank=True, to='main.Service')),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GroupName', models.CharField(max_length=900)),
                ('Messages', models.ManyToManyField(blank=True, to='main.Messages')),
            ],
        ),
        migrations.CreateModel(
            name='FrontPageFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(default='Normal', max_length=100)),
                ('Feedback', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.feedbacks')),
            ],
        ),
        migrations.AddField(
            model_name='feedbacks',
            name='Image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.images'),
        ),
    ]