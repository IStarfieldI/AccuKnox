from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
import time

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, created, **kwargs):
    print("Signal handler started")
    time.sleep(2)  
    print("Signal handler finished")


my_instance = MyModel.objects.create(name="Test")
print("Model saved")

#Django signals are executed synchronously by default.