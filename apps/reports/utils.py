from travello import settings
import os


def create_report_file(**kwargs):
    media_dir_path = settings.MEDIA_ROOT
    print(os.listdir(media_dir_path))
    if 'reports' not in os.listdir(media_dir_path):
        os.mkdir(os.path.join(media_dir_path, 'reports'))

    reports_dir_path = os.path.join(media_dir_path, 'reports')

    with open(f'{reports_dir_path}/report.txt', 'w', encoding='utf-8') as report:
        report.write(kwargs['report'])


def create_report_message(**kwargs):
    return f'''{kwargs['report_type']}

Дата: {kwargs['date']}
Агент: {kwargs['agent']}
Поставщик: {kwargs['supplier']}
Сумма агента: {kwargs['agent_sum']}
Сумма поставщика: {kwargs['supplier_sum']}
Направление: {kwargs['direction']}
Комментарий: {kwargs['comment']}
Маржа: {kwargs['marja']}    
'''


def create_agent_report_message(**kwargs):
    report_type = 'Отчет агент' if kwargs['repory_type'] == 'agent' else 'Отчет поставщик'
    return f'''{report_type}
    
Порядковый номер: {kwargs['serial_number']}
Дата: {kwargs['date']}
Сумма агента: {kwargs['agent_sum']}
Баланс: {kwargs['balance']}
Оплата агент: {kwargs['agent_payment']}
Направление: {kwargs['direction']}
Комментарий: {kwargs['comment']}
'''
