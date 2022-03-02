from django.db import models


class Table(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    count = models.IntegerField()
    distance = models.IntegerField()


    class Meta:
        verbose_name = 'Таблица'
        verbose_name_plural = 'Таблицы'

    def __str__(self):
        return self.name
