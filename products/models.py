from django.utils.translation import gettext_lazy as _
from django.db import models
# Create your models here.

class Products(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=70, db_column='name')
    picture = models.ImageField(verbose_name=_('Picture'), max_length=512, db_column="picture",upload_to="products/")
    price = models.FloatField(verbose_name=_('Price'), db_column="price")
    description = models.TextField(verbose_name=_('Description'), db_column='description')
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "products"
        verbose_name_plural = "product"
        managed = True
