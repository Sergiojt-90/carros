from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200, verbose_name="Modelo")
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand', verbose_name="Marca")
    factory_year = models.IntegerField(verbose_name="Ano de Fabricação")
    model_year = models.IntegerField(blank=True, null=True, verbose_name="Ano do Modelo")
    value = models.FloatField(blank=True, null=True, verbose_name="Valor")
    photo = models.ImageField(upload_to='cars/', blank=True, null=True, verbose_name="Foto")

    def __str__(self):
        return self.model
    


    


    