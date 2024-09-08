from django.db import models


class Menu(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Название меню'
    )
    description = models.TextField(
        verbose_name='Описание', max_length=300, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    cat = models.CharField(max_length=100, verbose_name='Категория')
    url = models.URLField(blank=True, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_items', default=None)

    class Meta:
        indexes = [models.Index(fields=['cat'])]
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.cat

    def get_url(self):
        return self.url