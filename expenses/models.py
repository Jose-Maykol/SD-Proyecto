
from datetime import datetime
from django.db import models

class Category(models.Model):

  name = models.CharField(default='', max_length= 20, verbose_name= 'Categoria de gasto')

  class Meta:

    verbose_name = 'Categoria'
    verbose_name_plural = 'Categorias'

  def __str__(self):
    return self.name

class Expenses(models.Model):

  amount = models.DecimalField(decimal_places=2, max_digits=10, verbose_name= 'Monto')
  category = models.ForeignKey(Category, on_delete= models.SET_DEFAULT, default= None, verbose_name= 'Categoria')
  date = models.DateTimeField(default= datetime.now ,blank=True, verbose_name='Fecha')

  class Meta:
    db_table = ''
    managed = True
    verbose_name = 'Gasto'
    verbose_name_plural = 'Gastos'
