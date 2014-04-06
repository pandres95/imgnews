from django.contrib import admin

# Including models
#from .fmodels.places import *
#from .fmodels.users import Usuario, Autor
#from .fmodels.posts import Post
#from .fmodels.users import Seguidor

from .models import *

# Register your models here.
class PostModel(admin.ModelAdmin):
    list_display = ("foto", "titulo","contenido","autor")


admin.site.register(Post, PostModel)
admin.site.register(Zona)

class LugarModel(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'


admin.site.register(Lugar, LugarModel)


# Register Users Models
class UserModel(admin.ModelAdmin):
    list_display = ("username", "first_name","last_name")

admin.site.register(Autor, UserModel)
admin.site.register(Seguidor, UserModel)
