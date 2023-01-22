from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

    # author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")

class Post(models.Model):
    title = models.CharField(max_length=125, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст")
    photo = models.ImageField(upload_to="phohtos/%Y/%m/%d/", blank=True, null=True, verbose_name="Фото")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, default='', verbose_name="Категория", related_name='posts')

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta():
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-create_at']


class Category(models.Model):
    name = models.CharField(max_length=128, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", default='')

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta():
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
