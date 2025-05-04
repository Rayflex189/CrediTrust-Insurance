from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('axis_app', '0003_alter_userprofile_profile_pic'),  # Update this
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='card_activation_token',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='card_activated',
            field=models.BooleanField(default=False),
        ),
    ]
