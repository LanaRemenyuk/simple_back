from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=150,
                            verbose_name='Имя',
                            help_text='Введите имя')
    contact_data = models.CharField(max_length=220,
                            null=True,
                            blank=True,
                            verbose_name='Контакты для связи',
                            help_text='Введите предпочтительный контакт для связи')
    specialty = models.CharField(max_length=150,
                                 verbose_name='Специальность',
                                 help_text='Вы по специальности')
    info = models.TextField(verbose_name='Информация о Вас',
                            help_text='Введите дополнительную информацию о Вас')

    class Meta:
        abstract = True


class CustomerProfile(Profile):

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'
        ordering = ['name']

    def __str__(self):
        return self.name


class ProviderProfile(Profile):
    experience_in_years = models.IntegerField(default=0,
                                              verbose_name='Опыт работы (лет)',
                                              help_text='Введите свой опыт работы в годах')

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'
        ordering = ['name']

    def __str__(self):
        return self.name
