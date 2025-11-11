from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Product, Contact


@receiver(post_save, sender=Product)
def product_created_handler(sender, instance, created, **kwargs):
    """Сигнал при создании нового товара"""
    if created:
        print(f"Создан новый товар: {instance.name}")


@receiver(post_save, sender=Contact)
def contact_created_handler(sender, instance, created, **kwargs):
    """Сигнал при создании нового контакта"""
    if created:
        print(f"Получено новое сообщение от: {instance.name}")