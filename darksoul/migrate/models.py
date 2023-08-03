from django.db import models


class contact(models.Model):
    name =models.CharField((""), max_length=50)
    email =models.CharField((""), max_length=50)
    subject =models.TextField((""))
    desc =models.TextField((""))

    def __str__(self):
        return self.name