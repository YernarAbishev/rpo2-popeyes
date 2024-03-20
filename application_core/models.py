from django.db import models

class Food(models.Model):
    name = models.CharField("Наименонивания блюда", max_length=100)
    description = models.CharField("Описание", max_length=255)
    image = models.CharField("Ссылка на фото", max_length=500)
    price = models.IntegerField("Цена")

    def __str__(self):
        return self.name