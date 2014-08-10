from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Note(models.Model):
    text = models.CharField(max_length=140)
    author = models.ForeignKey(User, related_name='notes')
    add_time = models.DateTimeField()
    last_update = models.DateTimeField()

    def save(self, *args, **kwargs):
        now = timezone.now()
        if self.add_time is None:
            self.add_time = now
        self.last_update = now
        super(Note, self).save(*args, **kwargs)

    def __str__(self):
        return ''.join([str(self.add_time), ': ', self.text[:10], '...'])

    class Meta:
        ordering = ('last_update',)
