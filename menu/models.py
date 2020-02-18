from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child', on_delete=models.SET_NULL)

    class Meta:
        ordering = ['name']
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menu:get_menu', args=[self.slug])

