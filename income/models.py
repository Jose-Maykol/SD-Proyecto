from datetime import datetime
from django.db import models

class Type(models.Model):
  name = models.CharField(default='', max_length= 20, verbose_name='Nombre de tipo de ingreso')

  class Meta:
    verbose_name = 'Tipo'
    verbose_name_plural = 'Tipos'

  def __str__(self):
    return self.name

class Income(models.Model):

  amount = models.DecimalField(decimal_places= 2, max_digits= 10, verbose_name= 'Monto')
  type = models.ForeignKey(Type, on_delete= models.SET_DEFAULT, default= None , verbose_name= 'Categoria')
  date = models.DateTimeField(default=datetime.now, blank=True ,verbose_name='Fecha')

  class Meta:
    verbose_name = 'Ingreso'
    verbose_name_plural = 'Ingresos'
