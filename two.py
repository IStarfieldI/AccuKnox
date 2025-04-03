import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def signal_handler(sender, instance, created, **kwargs):
    print(f"Signal thread: {threading.current_thread().name}")

print(f"Caller thread: {threading.current_thread().name}")
my_instance = MyModel.objects.create(name="Test")
#Yes, Django signals run in the same thread as the caller by default