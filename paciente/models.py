from django.db import models
from django.utils import timezone


class Terapeuta(models.Model):
    terapeuta = models.CharField(max_length=150)
    rut = models.CharField(max_length=9)

    def __str__(self):
        return self.terapeuta

class Hora(models.Model):
    paciente = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    terapeuta = models.ForeignKey(Terapeuta, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(
            default=timezone.now)
    fecha_atencion = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.fecha_creacion = timezone.now()
        self.save()

    def __str__(self):
        return str(self.fecha_atencion)


