from django.contrib import admin
from odorwatch.models import Cliente, UnidadFiscalizable, Documento, Coincidencias, Palabras
from .models import Usuario,LogsUsuario
# Registra de los modelos para admin
admin.site.register(Cliente)
admin.site.register(UnidadFiscalizable)
admin.site.register(Documento)
admin.site.register(Coincidencias)
admin.site.register(Palabras)
admin.site.register(Usuario)
admin.site.register(LogsUsuario)
