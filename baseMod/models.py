from django.conf import settings
from django.contrib.auth.models import User as Auth_User
from django.db import models
from django_extensions.db.fields import UUIDField
from django.core.files.storage import FileSystemStorage

# Create your models here.
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

class Usuario(Auth_User):
    vivienda = models.ManyToManyField(Zona)
    pass


class Autor(Usuario):
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        pass
    def __str__(self):
        return "Autor: %s" % self.usuario.id
    pass


fs = FileSystemStorage(location='/home/fabian_martinez/Documentos/imgnews/media/')

class Post(models.Model):
    id = UUIDField(primary_key = True)
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(Autor)
    contenido = models.TextField()
    ubicacion = models.ForeignKey(Lugar)
    foto = models.ImageField(storage=fs, upload_to='post_imgs/%Y/%m/%d')

    @property
    def filename(self):
        return os.path.basename(self.id)
    pass


class Seguidor(Usuario):
    class Meta:
        verbose_name = 'Seguidor'
        verbose_name_plural = 'Seguidores'
        pass
    likes = models.ManyToManyField(Post, blank = True)
    is_admin = False
    def __str__(self):
        return "Seguidor: %s" % self.usuario.id
    pass
