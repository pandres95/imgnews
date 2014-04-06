from django.conf import settings
from django.db import models

from django.core.files.storage import FileSystemStorage
from django_extensions.db.fields import UUIDField

from django.contrib.auth.models import User as Auth_User

from places import Zona, Lugar

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


fs = FileSystemStorage(location=settings.MEDIA_ROOT)
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
