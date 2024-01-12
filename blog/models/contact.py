from django.db import models

class ContactModel(models.Model):
    name_surname = models.CharField(max_length=100, blank=False)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        db_table = 'contact'
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'

    def __str__(self):
        return self.email