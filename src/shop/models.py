from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):

   name =  models.CharField(max_length=30,db_index=True)
   slug = models.SlugField(max_length=50,db_index=True,unique=True)

   class Meta:

      ordering=('name',)
      verbose_name='Category'
      verbose_name_plural = 'Catigories'

   def __str__(self):
       return self.name


class Product(models.Model):
   category = models.ForeignKey(Category,on_delete=None)
   name = models.CharField(max_length=30,db_index=True)
   slug = models.SlugField(max_length=50, db_index=True, unique=True)
   image = models.ImageField(blank=True,upload_to='static/products')
   descp = models.TextField(blank=True)
   stock = models.PositiveIntegerField()
   price = models.DecimalField(max_digits=10,decimal_places=2)
   avilable = models.BooleanField(default=True)
   featured = models.BooleanField(default=False)
   special = models.BooleanField(default=False)
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)

   class Meta:
      verbose_name = 'Product'
      verbose_name_plural  = 'Products'

   def __str__(self):
       return self.name

   def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.slug, self.id])
