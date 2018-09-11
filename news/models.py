from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()



class Category(models.Model):
    """"Класс категорий статей"""
    title = models.CharField("Название", max_length=50)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title

class Tag(models.Model):
    """"Класс тегов статей"""
    title = models.CharField("Тэг", max_length=50)

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.title


class News(models.Model):
    """"Класс новостей
    """
    user = models.ForeignKey(User, verbose_name= 'Автор', on_delete=models.SET_NULL, null=True)
    title = models.CharField("Заголовок", max_length=100)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    text_min = models.TextField("Короткое описание", max_length=350)
    text = models.TextField("Текст статьи")
    tags = models.ManyToManyField(Tag, verbose_name="Тэги")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    description = models.CharField("Описание", max_length=150)
    keywords = models.CharField("Ключевые слова", max_length=100)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title

class Comments(models.Model):
   
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.SET_NULL, null=True ) # CASCADE означает если пользователь будет удален, то все его комментарии также будут удалены
    new = models.ForeignKey(News, verbose_name="Новость", on_delete=models.SET_NULL, null=True)
    text = models.TextField("Короткое описание", max_length=1000)
    created = models.DateTimeField("Дата добавления", auto_now_add=True, null=True)
    moderation = models.BooleanField("Модерация", default=False)


    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Коментарии"

    def __str__(self):
        return "{}".format(self.user)
