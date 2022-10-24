from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateField(auto_now_add=True)
    time_update = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title  # возвращает заголовок текущей записи

    def get_absolute_url(self):
        """
        Формирует абсолютный url для шаблона
        :return:
        """
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        """
        Отображает имя приложения в админ панели в ед. и множественном числе
        """
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
        ordering = ['time_create', 'title']  # сортировка по времени


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Формирует абсолютный url для шаблона
        :return:
        """
        return reverse('category', kwargs={'cat_id': self.pk})
