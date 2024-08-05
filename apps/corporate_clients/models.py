from django.db import models

# Create your models here.


def license_upload_to(instance, filename):
    return 'corporate_clients/{name}/licenses/{filename}'.format(filename=filename, name=instance.name)


class CorporateClientRequest(models.Model):
    class ClientTypeChoices(models.TextChoices):
        OWNER = 'OWNER', 'Владелец компании'
        HR = 'HR', 'HR компании'
        DIRECTOR = 'DIRECTOR', 'Директор компании'

        __empty__ = 'Не выбрано'

    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона')
    about_company = models.TextField(verbose_name='О компании', blank=True, null=True)
    client_type = models.CharField(verbose_name='Тип клиента', max_length=10, choices=ClientTypeChoices.choices)
    khakimiyat_license = models.FileField(verbose_name='Лицензия из хакимиата', upload_to=license_upload_to)
    uzb_tourism_license = models.FileField(verbose_name='Лицензия от коммитета туризма УЗБ', upload_to=license_upload_to)
    lease_contract = models.FileField(verbose_name='Догор аренды', upload_to=license_upload_to)
    director_passport = models.FileField(verbose_name='Паспорт директора', upload_to=license_upload_to)
    charter = models.FileField(verbose_name='Устав', upload_to=license_upload_to)
    address_and_index = models.CharField(max_length=150, verbose_name='Адрес и индекс')
    fax = models.CharField(verbose_name='Факс', max_length=150)
    corparate_account = models.CharField(max_length=150, verbose_name='К/счет')
    mfo = models.CharField(max_length=150, verbose_name='МФО')
    okonx = models.CharField(max_length=150, verbose_name='ОКОНХ')
    okpo = models.CharField(max_length=150, verbose_name='ОКПО')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name}: {self.phone_number}'
    
    class Meta:
        verbose_name = 'Заявка корпоративного клиента'
        verbose_name_plural = 'Заявки корпоративных клиентов'
