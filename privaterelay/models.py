from django.db import models


class Invitations(models.Model):
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    date_sent = models.DateTimeField()
    date_redeemed = models.DateTimeField()

    def __str__(self):
        return 'Invitation for ' % self.email
