from django.conf import settings
from django.db import models

class Zona(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    pass


class Lugar(models.Model):
    class Meta:
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'
        pass
    nombre = models.CharField(max_length=255, default=None, blank=True, null=True)
    lat = models.DecimalField(max_digits=10,decimal_places=7)
    lng = models.DecimalField(max_digits=10,decimal_places=7)
    zona = models.ForeignKey(Zona)

    def __str__(self):
        return "%s ubicado en %s: (%d, %d)" % (self.nombre, self.zona.nombre, self.lat, self.lng)
    pass
