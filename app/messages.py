normal_values = {
    "floor": [1, 50],
    "number_of_floors": [1, 80],
    "min_to_metro": [1, 30],
    "total_area": [20, 250],
    "living_area": [1, 150],
    "ceiling_height": [2.3, 5],
    "construction_year": [1940, 2030],
    "price": [8*10**6, 2.5*10**8]
}

names = {
    "min_to_metro": "Минут до метро",
    "total_area": "Общая площадь",
    "living_area": "Жилая площадь",
    "floor": "Этаж",
    "number_of_floors":	"Этажей в доме",
    "construction_year": "Год постройки",
    "is_new": "Тип жилья",
    "is_apartments": "Апартаменты",
    "ceiling_height": "Высота потолка",
    "number_of_rooms": "Количество комнат",
    "region_of_moscow": "Округ Москвы"
}

field_is_required_message = 'Это обязательное поле'

normal_values_messages = {}
for i in normal_values:
    normal_values_messages[i] = f"Введите значение от {normal_values[i][0]} до {normal_values[i][1]}"

regoins_choices = dict(enumerate(['ВАО', 'ЗАО', 'САО', 'СВАО', 'СЗАО', 'ЦАО', 'ЮАО', 'ЮВАО', 'ЮЗАО']))
yes_no_choices = {1: "Да", 0: "Нет"}
is_new_choices = {1: "Первичка", 0: "Вторичка"}
rooms_choices = dict([(i+1, i+1) for i in range(4)])


def prediction_readable(pred: float):
    return f"{int(round(pred, -3)):,}"