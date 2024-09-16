from django.db import models
from apps.users.models import User

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


class DailySales(models.Model):
    # serial_number = models.IntegerField(verbose_name='Порядковый номер')
    date = models.DateField(verbose_name='Дата')
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

    class Meta:
        verbose_name = 'Дневная продажа'
        verbose_name_plural = 'Дневные продажи'


class AgentReport(models.Model):
    serial_number = models.IntegerField(verbose_name='Порядковый номер')
    date = models.DateField(verbose_name='Дата')
    agent_sum = models.IntegerField(verbose_name='Сумма агент')
    direction = models.TextField(verbose_name='Направление')
    agent_payment = models.IntegerField(verbose_name='Оплата агент')
    balance = models.IntegerField(verbose_name='Баланс')
    comment = models.TextField(verbose_name='Комментарий')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Сотрудник')

    def __str__(self):
        return str(self.serial_number)

    class Meta:
        verbose_name = 'отчет агент'
        verbose_name_plural = 'отчет агент'


class SupplierReport(models.Model):
    serial_number = models.IntegerField(verbose_name='Порядковый номер')
    date = models.DateField(verbose_name='Дата')
    agent_sum = models.IntegerField(verbose_name='Сумма агент')
    direction = models.TextField(verbose_name='Направление')
    agent_payment = models.IntegerField(verbose_name='Оплата агент')
    balance = models.IntegerField(verbose_name='Баланс')
    comment = models.TextField(verbose_name='Комментарий')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Сотрудник')

    def __str__(self):
        return str(self.serial_number)

    class Meta:
        verbose_name = 'Отчет поставщик'
        verbose_name_plural = 'Отчет поставщик'
