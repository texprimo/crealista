from django.contrib import admin
from slista.models import *
# from django.contrib.auth.models import *

# MenuAdmin e RigaInline sono inseriti per visualizzazione Padre-Figlio Menu-Righe di menu
class RigaInLine(admin.TabularInline):
   model=Riga

class MenuAdmin(admin.ModelAdmin):
   inlines=[RigaInLine,]

# VoceAdmin e ComposizioneInline sono inserite per visualizzazione Padre-Figlio degli ingredienti
class ComposizioneInline(admin.TabularInline):
   model=Composizione
   fk_name="prodotto"
   extra=1

class VoceAdmin(admin.ModelAdmin):
   inlines=[ComposizioneInline,]

# UMAdmin e TrasformatoreInline sono inserite per visualizzazione delle conversioni fra unità di misura
class TrasformatoreInline(admin.TabularInline):
   model=Trasformatore
   fk_name="UMEntrata"
   extra=1

class UMAdmin(admin.ModelAdmin):
   inlines=[TrasformatoreInline,]

# Register your models here.

#admin.site.register(Utente)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Voce, VoceAdmin)
#admin.site.register(Composizione)
admin.site.register(UM, UMAdmin)
#admin.site.register(Trasformatore)
#admin.site.register(Riga)


