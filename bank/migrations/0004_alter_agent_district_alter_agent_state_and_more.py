# Generated by Django 5.1.2 on 2024-10-26 18:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_alter_agent_district_alter_agent_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.district'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.state'),
        ),
        migrations.AlterField(
            model_name='agentassignedtobank',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.district'),
        ),
        migrations.AlterField(
            model_name='agentassignedtobank',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.state'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.district'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.state'),
        ),
        migrations.AlterField(
            model_name='bankabout',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.district'),
        ),
        migrations.AlterField(
            model_name='bankabout',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.state'),
        ),
        migrations.AlterField(
            model_name='bankprivacypolicy',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.district'),
        ),
        migrations.AlterField(
            model_name='bankprivacypolicy',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.state'),
        ),
        migrations.AlterField(
            model_name='userassignedtobank',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.district'),
        ),
        migrations.AlterField(
            model_name='userassignedtobank',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.state'),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.district'),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.state'),
        ),
        migrations.AlterField(
            model_name='userloanaddstatement',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.district'),
        ),
        migrations.AlterField(
            model_name='userloanaddstatement',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.state'),
        ),
        migrations.AlterField(
            model_name='userloanstatement',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.district'),
        ),
        migrations.AlterField(
            model_name='userloanstatement',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.state'),
        ),
        migrations.AlterField(
            model_name='userpaymentstatement',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.district'),
        ),
        migrations.AlterField(
            model_name='userpaymentstatement',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.state'),
        ),
    ]