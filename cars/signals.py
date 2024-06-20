from django.db.models.signals import pre_save, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory
from gemini_api.client import get_car_descriptionAI

def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value = Sum('value')
    )['total_value']
    CarInventory.objects.create(
        cars_count = cars_count,
        cars_value = cars_value
    )


@receiver(pre_save, sender=Car)
def car_presave(sender, instance, **kwargs):
    
    if not instance.description:
        instance.description = 'Descrição indisponível'


    # CONFIGURAÇÃO PARA GERAR DESCRIÇÃO POR IA, UTILIZE ESTA ABAIXO.
    
    # if not instance.description:
    #     ai_description = get_car_descriptionAI(instance.model, instance.brand, instance.model_year)
    #     instance.description = ai_description

@receiver(post_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    car_inventory_update()


@receiver(post_delete, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    car_inventory_update()