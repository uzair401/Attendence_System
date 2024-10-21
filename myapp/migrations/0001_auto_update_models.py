from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),  # Replace with the correct migration file if needed
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='staff_leave',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='staff_leave',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
