from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class File(models.Model):
    name = models.CharField(max_length=1024)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    directory = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    resource = models.FileField()

    FILE_TYPE_CHOICES = (
        ('F', 'file'),
        ('D', 'directory'),
    )

    file_type = models.CharField(choices=FILE_TYPE_CHOICES, max_length=100, default='F')


@receiver(post_save, sender=User)
def create_user_home_directory(sender, instance, created, **kwargs):
    if created:
        File.objects.create(name='Home', owner=instance, file_type='D')
