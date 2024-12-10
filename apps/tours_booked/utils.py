def create_event_booked_message(data: dict):
    tourists = []

    _tourists = data.get("tourists")

    for tourist in _tourists:
        tourists.append(
            f"""
Имя: {tourist['first_name']}
Фамилия: {tourist['lastname']}
Дата рождения: {tourist['birth_date']}
Серия и номер паспорта: {tourist['passport_seria_and_number']}
Дата окончания паспорта: {tourist['expiration_date']}
Пол: {tourist['gender']}
Гражданство: {tourist['citizen']}
        """
        )

    return f"""
Бронь тура: {data['event']}

Пользователь: {data['user']}
Количество взрослых: {data['total_adult']}
Количество детей: {data['total_children']}

Данные отдыхающих:
{'\n'.join(tourists)}

Тип тура: {data['event_type']}
"""
