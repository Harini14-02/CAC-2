from django.db import models

# Create your models here.
class booking(models.Model):
    name = models.CharField(blank=False,max_length=50)
    activity = models.TextField(blank=False,max_length=250)
    destination = models.CharField(blank=False,max_length=200)
    date = models.DateField(blank=False)

    def _str_(self):
        return str(self.name._str_())