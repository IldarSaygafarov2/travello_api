from django.db import models
from apps.users.models import User
from datetime import datetime

"""
форма дневной продажи:

номер   порядковые номера
дата   30.12.2023
агент  выпадающий список с автозаполнением
поставщик выпадающий список с автозаполнением
сумма агент  число
сумма поставщик число
направление текст alphanumeric
комментарий текст alphanumeric
маржа число
"""


class Agent(models.Model):
    name = models.CharField(max_length=255, verbose_name='Агент')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Агент'
        verbose_name_plural = 'Агенты'
        ordering = ['name']


class Supplier(models.Model):
    name = models.CharField(max_length=255, verbose_name='Поставщик')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ['name']


class DailySaleItem(models.Model):
    date = models.DateField(default=datetime.today().strftime('%Y-%m-%d'), verbose_name='Дата')
    passenger = models.CharField(verbose_name='Пассажир', max_length=100)
    direction = models.CharField(verbose_name='Направление', max_length=100)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, verbose_name='Агент')
    agent_sum = models.FloatField(verbose_name='Сумма агент', default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, verbose_name='Поставщик', null=True)
    supplier_sum = models.FloatField(verbose_name='Сумма поставщик', default=0)
    margin = models.FloatField(verbose_name='Маржа', default=0)
    comment = models.TextField(verbose_name='Комментарий', default='', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.marja = self.agent_sum - self.supplier_sum
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.pk} - {self.date}'

    class Meta:
        verbose_name = 'Дневная продажа'
        verbose_name_plural = 'Дневные продажи'


class DailySales(models.Model):
    date = models.DateField(verbose_name='Дата', default=datetime.today().strftime('%Y-%m-%d'))
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, verbose_name='Агент', related_name='daily_sales')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='Поставщик',
                                 related_name='daily_sales')
    agent_sum = models.IntegerField(verbose_name='Сумма агента')
    supplier_sum = models.IntegerField(verbose_name='Сумма поставщика')
    direction = models.TextField(verbose_name='Направление')
    comment = models.TextField(verbose_name='Комментарий')
    marja = models.IntegerField(verbose_name='Маржа')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Сотрудник')

    def __str__(self):
        return str(self.pk)

    def save(self, *args, **kwargs):
        self.marja = self.supplier_sum - self.agent_sum
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Дневная продажа'
        verbose_name_plural = 'Дневные продажи'


class AgentReport(models.Model):
    date = models.DateField(verbose_name='Дата')
    direction = models.TextField(verbose_name='Направление')
    agent_sum = models.IntegerField(verbose_name='Сумма агент')
    agent_payment = models.IntegerField(verbose_name='Оплата агент')
    balance = models.IntegerField(verbose_name='Баланс')
    comment = models.TextField(verbose_name='Комментарий')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Сотрудник')

    # def get_fields_names(self):
    #     print(self._meta.fields)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'отчет агент'
        verbose_name_plural = 'отчет агент'


class SupplierReport(models.Model):
    date = models.DateField(verbose_name='Дата')
    agent_sum = models.IntegerField(verbose_name='Сумма агент')
    direction = models.TextField(verbose_name='Направление')
    agent_payment = models.IntegerField(verbose_name='Оплата агент')
    balance = models.IntegerField(verbose_name='Баланс')
    comment = models.TextField(verbose_name='Комментарий')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Сотрудник')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Отчет поставщик'
        verbose_name_plural = 'Отчет поставщик'
