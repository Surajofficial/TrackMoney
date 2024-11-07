# Generated by Django 5.1.2 on 2024-11-03 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_alter_agent_district_alter_agent_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='photo',
            field=models.FileField(upload_to='media/agent_photos/'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='uid_doc',
            field=models.FileField(upload_to='media/agent_uid_docs/'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='bank_logo',
            field=models.FileField(upload_to='media/bank_logos/'),
        ),
        migrations.AlterField(
            model_name='bankabout',
            name='about_doc',
            field=models.FileField(upload_to='media/bank_about_docs/'),
        ),
        migrations.AlterField(
            model_name='bankprivacypolicy',
            name='policy_doc',
            field=models.FileField(upload_to='media/bank_privacy_policies/'),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='uid_doc',
            field=models.FileField(upload_to='media/user_uid_docs/'),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='user_photo',
            field=models.FileField(upload_to='media/user_photos/'),
        ),
        migrations.AlterField(
            model_name='userloanaddstatement',
            name='agreement_copy',
            field=models.FileField(blank=True, null=True, upload_to='media/loan_agreements/'),
        ),
    ]