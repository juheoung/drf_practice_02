from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Card(models.Model):
    number = models.IntegerField(null=False)
    shape = models.CharField(max_length=10, null=False)
    create = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='Card', on_delete=models.CASCADE)

    def __str__(self):
        return self.shape

    class Meta:
        ordering = ['create']


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
