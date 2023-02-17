from django.db import models


class Zoo(models.Model):
    animal_type = models.CharField(max_length=50, verbose_name="Вид животного")
    name = models.CharField(max_length=50, verbose_name="Класс")
    image = models.ImageField(upload_to="%Y/%m/%d/", verbose_name="Изображение")
    description = models.TextField(blank=False, verbose_name="Краткое описание животного")
    date_of_added = models.DateTimeField(auto_now_add=True, verbose_name="Дата написания статьи")

    class Meta:
        verbose_name = "Животное"
        verbose_name_plural = "Животные"

    def __str__(self):
        return self.name