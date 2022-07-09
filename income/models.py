from unicodedata import category
from django.db import models

class Category(models.Model):
  name = models.CharField(default=' ', max_length= 20, verbose_name='Nombre de categoria')
  class Meta:
    verbose_name = 'Categoria'
    verbose_name_plural = 'Categorias'

  def __str__(self):
    return self.name

class Income(models.Model):

  amount = models.DecimalField(decimal_places= 2, max_digits= 10, verbose_name= 'Monto')
  category = models.ForeignKey(Category, on_delete= models.SET_DEFAULT, default= None , verbose_name= 'Categoria')
  class Meta:
    verbose_name = 'Ingreso'
    verbose_name_plural = 'Ingresos'
