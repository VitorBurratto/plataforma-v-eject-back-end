from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def set_is_staff(sender, instance, created, **kwargs):
    if created and not instance.is_staff:
        instance.is_staff = True
        instance.save()
        
# toda vez que um usuário ele faz login, já vira automáticamente membro da equipe no admin