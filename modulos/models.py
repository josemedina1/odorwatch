from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=255)
    rol = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    

class LogsUsuario(models.Model):
    accion = models.CharField(max_length=255)
    fecha_hora = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="logs")

    def __str__(self):
        return f"Log de {self.usuario} - {self.fecha_hora}"


class LogsError(models.Model):
    nombre_error = models.CharField(max_length=255)
    codigo_error = models.CharField(max_length=50, null=True, blank=True)
    hora_error = models.TimeField()
    fecha_error = models.DateField()
    tipo_error = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name="logs_error")

    def __str__(self):
        return self.nombre_error