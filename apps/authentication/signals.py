from .models import Users
from django.db.models.signals import post_save
from django.dispatch import receiver
from .active_account import ActiveAccount



#posso salvar algo no banco de dados pela propia funcao de sinal
# ex: quando um dado 'e salvo, posso salvar algo a mais a parir do sender
@receiver(post_save, sender=Users)
def active_account_mail(sender: Users, instance: Users, created, **kwargs):
    if created and not instance.is_active:
        active_account = ActiveAccount(instance)
        active_account.active_account_send_mail()