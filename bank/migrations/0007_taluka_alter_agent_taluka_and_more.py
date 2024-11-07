# Generated by Django 5.1.2 on 2024-11-03 08:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0006_alter_agent_photo_alter_agent_uid_doc_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taluka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('district', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='bank.district')),
                ('state', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='bank.state')),
            ],
        ),
        migrations.AlterField(
            model_name='agent',
            name='taluka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.taluka'),
        ),
        migrations.AlterField(
            model_name='agentassignedtobank',
            name='taluka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.taluka'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='taluka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.taluka'),
        ),
        migrations.AlterField(
            model_name='bankabout',
            name='taluka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.taluka'),
        ),
        migrations.AlterField(
            model_name='bankprivacypolicy',
            name='taluka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.taluka'),
        ),
        migrations.AlterField(
            model_name='userassignedtobank',
            name='taluka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.taluka'),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='taluka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.taluka'),
        ),
        migrations.AlterField(
            model_name='userloanaddstatement',
            name='taluka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.taluka'),
        ),
        migrations.AlterField(
            model_name='userloanstatement',
            name='taluka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.taluka'),
        ),
        migrations.AlterField(
            model_name='userpaymentstatement',
            name='taluka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.taluka'),
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('district', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='bank.district')),
                ('state', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='bank.state')),
                ('taluka', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='bank.taluka')),
            ],
        ),
        migrations.AlterField(
            model_name='agent',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.village'),
        ),
        migrations.AlterField(
            model_name='agentassignedtobank',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.village'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.village'),
        ),
        migrations.AlterField(
            model_name='bankabout',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.village'),
        ),
        migrations.AlterField(
            model_name='bankprivacypolicy',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.village'),
        ),
        migrations.AlterField(
            model_name='userassignedtobank',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.village'),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.village'),
        ),
        migrations.AlterField(
            model_name='userloanaddstatement',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.village'),
        ),
        migrations.AlterField(
            model_name='userloanstatement',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.village'),
        ),
        migrations.AlterField(
            model_name='userpaymentstatement',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.village'),
        ),
    ]