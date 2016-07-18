from django.db import models
from django.utils import timezone


class Beliefs(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    """
    def save(self, *args, **kwargs):
        # do_something()
        super(Blog, self).save(*args, **kwargs) # Call the "real" save() method.
        # do_something_else()
    """
