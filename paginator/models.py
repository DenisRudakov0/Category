from django.db import models

class Product(models.Model):
    title = models.CharField('Название', max_length = 50)
    anons = models.CharField('Ссылка на фото', max_length = 50)
    full_text = models.TextField('Описание товара')
    cena = models.CharField('Цена', max_length = 10)
    cena_action = models.CharField('Цена со скидкой', max_length = 10)
    date = models.DateTimeField('Дата публикации')
    date_start = models.DateTimeField('Дата начала акции')
    date_end = models.DateTimeField('Дата окончания акции')

    def __str__(self):
        return f'Новость: {self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date']
