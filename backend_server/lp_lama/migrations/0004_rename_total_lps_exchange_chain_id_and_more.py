# Generated by Django 4.1 on 2022-08-28 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lp_lama', '0003_lp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exchange',
            old_name='total_lps',
            new_name='chain_id',
        ),
        migrations.RemoveField(
            model_name='lp',
            name='chain_ids',
        ),
        migrations.AddField(
            model_name='exchange',
            name='address',
            field=models.CharField(default='a', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exchange',
            name='reward_address',
            field=models.CharField(default='a', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lp',
            name='pool_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exchange',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='lp',
            name='address',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='exchange',
            unique_together={('address', 'chain_id')},
        ),
        migrations.RemoveField(
            model_name='exchange',
            name='chain_ids',
        ),
    ]
