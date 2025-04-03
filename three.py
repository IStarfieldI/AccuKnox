from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models, transaction

class MyModel(models.Model):
    name = models.CharField(max_length=100)

class AnotherModel(models.Model):
    data = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def signal_handler(sender, instance, created, **kwargs):
    AnotherModel.objects.create(data="Signal Data")
try:
    with transaction.atomic():
        my_instance = MyModel.objects.create(name="Test")
        
except Exception as e:
    print(e)

print(AnotherModel.objects.all())
#Yes, by default, Django signals run in the same database transaction as the caller