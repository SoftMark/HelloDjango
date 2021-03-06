import subprocess
from django.db import models
from django.utils.safestring import mark_safe
from django.db.models.signals import pre_save, post_init, post_save
from django.core.files.base import File
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from ckeditor.fields import RichTextField
import moviepy.editor as moviepy
import os



class GalleryImage(models.Model):
    image_name = models.CharField('Название картинки', max_length=50)
    image = models.ImageField(verbose_name='Изображение', upload_to='gallery', default=None)
    small_image = ImageSpecField(source='image',
                                 processors=[ResizeToFill(300, 200)],
                                 format='JPEG',
                                 options={'quality': 60})

    def image_img(self):
        if self.image:
            return mark_safe(u'<a class="all-photo" href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(
                self.image.url))
        else:
            return '(Нет изображения)'

    def small_image_img(self):
        if self.small_image:
            return mark_safe(u'<a class="all-photo" href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(
                self.small_image.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Изображение'
    image_img.allow_tags = True

    def __str__(self):
        return self.image_name

    class Meta:
        verbose_name = 'Изображение для галереи'
        verbose_name_plural = 'Галерея'


# Create your models here.
class Chihuahua(models.Model):
    name = models.CharField('Имя', max_length=50)
    gender = models.CharField(choices=(('female', "сука"), ('male', "кобель")), verbose_name='Пол', max_length=20,
                              default='female')
    rewards = models.TextField('Награды')

    birth_date = models.DateField('Дата рождения')
    age = models.CharField(choices=(('puppy', "щенок"), ('adult', "взрослый")), verbose_name='Щенок/Взрослый',
                           max_length=20, default='adult')
    sale = models.CharField(choices=(('Да', "Да"), ('Нет', "Нет")), verbose_name='Для продажи',
                            max_length=20, default='Да')
    reserve = models.CharField(choices=(('Да', "Да"), ('Нет', "Нет")), verbose_name='В резерве',
                               max_length=20, default='Нет')
    teeth = models.CharField('Зубы', max_length=7)
    weight = models.FloatField('Вес')
    color = models.TextField('Окрас')
    type_of_wool = models.CharField('Тип шерсти', max_length=25)
    father = models.CharField('Папа', max_length=50)
    mother = models.CharField('Мама', max_length=50)
    pedigree = models.CharField('Родословная', max_length=50)
    pedigree_link = models.URLField('Ссылка на родословную')
    video = models.FileField(upload_to="videos", null=True, verbose_name='Видео', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Чихуахуа'
        verbose_name_plural = 'Чишки'


class Photo(models.Model):
    # image = DynamicUploadImageField(blank=True)
    image = models.ImageField(verbose_name='Фото', upload_to='photos')
    small_image = ImageSpecField(source='image',
                                 processors=[ResizeToFill(800, 600)],
                                 format='JPEG',
                                 options={'quality': 60})

    thumb_image = ImageSpecField(source='image',
                                 processors=[ResizeToFill(300, 200)],
                                 format='JPEG',
                                 options={'quality': 60})

    @classmethod
    def image_no_photo(cls):
        no_photo_url = "/content/images/no_photo.jpg"
        return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(no_photo_url))

    def image_img(self):
        if self.image:
            return mark_safe(
                f'<a class="all-photo" href="{self.image.url}" target="_blank"><img src="{self.small_image.url}" width="100"/></a>')
        else:
            return self.image_no_photo()

    chihuahua = models.ForeignKey(Chihuahua, on_delete=models.CASCADE, related_name='images')

    def small_image_img(self):
        if self.small_image:
            return mark_safe(u'<a class="all-photo" href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(
                self.small_image.url))
        else:
            return '(Нет изображения)'


# Create settings content
# class Content(models.Model):


class SiteConfigurations(models.Model):
    # Favicon
    favicon = models.ImageField("Favicon", default="/favicon.ico")

    # Main
    name = models.CharField('Название шаблона', max_length=50, default='Основной')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Конфигурации'
        verbose_name_plural = 'Конфигурации'

    # Header
    title = models.CharField('Заголовок', max_length=25, default="Выбери себе нового друга!")
    inst = models.URLField('Instagram ссылка')
    facebook = models.URLField('FaceBook ссылка')
    header_background = models.ImageField(verbose_name='Фон шапки', upload_to='gallery')
    # header_m_background = models.ImageField(verbose_name='Фон шапки(смартфон)', upload_to='gallery', default=None)

    def header_get_background(self):
        if self.header_background:
            return mark_safe(u'<a class="all-photo" href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(
                self.header_background.url))
        else:
            return '(Нет изображения)'

    header_get_background.short_description = 'Верхнее изображение'
    header_get_background.allow_tags = True

    # About us
    a_us_t_image = models.ImageField(verbose_name='Верхнее изображение', upload_to='gallery')
    a_us_t_paragraph = RichTextField('Верхний параграф', blank=True)
    #a_us_t_paragraph = models.TextField('Верхний параграф', blank=True)
    a_us_b_image = models.ImageField(verbose_name='Нижнее изображение', upload_to='gallery')
    a_us_b_paragraph = RichTextField('Нижний параграф', blank=True)
    #a_us_b_paragraph = models.TextField('Нижний параграф', blank=True)
    #rich_text = RichTextField(default='', name='Rich')


    def get_a_us_t_image(self):
        if self.a_us_t_image:
            return mark_safe(u'<a class="all-photo" href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(
                self.a_us_t_image.url))
        else:
            return '(Нет изображения)'

    get_a_us_t_image.short_description = 'Верхнее изображение'
    get_a_us_t_image.allow_tags = True

    def get_a_us_b_image(self):
        if self.a_us_b_image:
            return mark_safe(u'<a class="all-photo" href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(
                self.a_us_b_image.url))
        else:
            return '(Нет изображения)'

    get_a_us_b_image.short_description = 'Нижнее изображение'
    get_a_us_b_image.allow_tags = True

    # Footer
    footer_title = models.CharField('Заголовок', max_length=30, default="Заголовок футера")
    first_phone = models.CharField('Первый номер телефона', max_length=20, default="+38(0**)-***-**-**", blank=True)
    first_viber_flag = models.CharField(choices=(('Да', "Да"), ('Нет', "Нет")), verbose_name='Вайбер',
                               max_length=5, default='Нет', blank=True)
    second_phone = models.CharField('Второй номер телефона', max_length=20, default="+38(0**)-***-**-**", blank=True)
    second_viber_flag = models.CharField(choices=(('Да', "Да"), ('Нет', "Нет")), verbose_name='Вайбер',
                               max_length=5, default='Нет', blank=True)
    face_name = models.CharField('FaceBook(Имя)', max_length=25, default="Мой логин FaceBook", blank=True)
    inst_name = models.CharField('Instagram(Имя)', max_length=25, default="Мой логин Instagram", blank=True)
