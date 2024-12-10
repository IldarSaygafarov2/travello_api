from datetime import datetime


def msg_for_corporate_client_request(data):
    created_at = datetime.fromisoformat(data["created_at"]).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    msg = f"""
Имя: {data['name']}
Почта:  {data['email']}
Номер телефона: {data['phone_number']}
О компании: {data['about_company']}
Должность клиента: {data['client_type']}
Адрес и индекс: {data['address_and_index']}
Факс: {data['fax']}
К/счет: {data['corparate_account']}
МФО: {data['mfo']}
ОКОНХ: {data['okonx']}
ОКЛО: {data['okpo']}

Дата отправки: {created_at}
"""
    return msg


def get_documents_urls(data):
    result = []
    fields = {
        "khakimiyat_license": "Лицензия из хакимиата",
        "uzb_tourism_license": "Лицензия от коммитета туризма УЗБ",
        "lease_contract": "Договор аренды",
        "director_passport": "Паспорт директора",
        "charter": "Устав",
    }
    for key, value in data.items():
        if key in fields:
            result.append((fields[key], value))
    return result
