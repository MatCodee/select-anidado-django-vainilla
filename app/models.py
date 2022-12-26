from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=300,verbose_name='Nombre')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']
        
        
class Product(models.Model):
    name = models.CharField(max_length=300,verbose_name='Nombre')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']