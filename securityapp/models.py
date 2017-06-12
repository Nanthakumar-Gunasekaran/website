from django.db import models
from django.core.urlresolvers import reverse


class Account(models.Model):
    account_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    user_first_name = models.CharField(max_length=100)
    user_last_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('securityapp:index', kwargs={'pk': self.pk})

    def __str__(self):
        return self.account_name
