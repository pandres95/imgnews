from django.contrib import admin
from .models import Post, Autor, Seguidor, Zona, Lugar

# Register your models here.
admin.site.register(Post)
admin.site.register(Autor)
admin.site.register(Seguidor)
admin.site.register(Zona)
admin.site.register(Lugar)
