import pandas as pd
from point import Point

def process_excel(file_path):
    """
    Чтение и обработка данных из Excel файла, создание объектов Point

    :param file_path: Путь к файлу Excel.
    :return: Словарь с объектами Point.
    """
    df = pd.read_excel(file_path)

    # Сортировка данных по столбцу "День приема заказа"
    df.sort_values(by="День приема заказа", inplace=True)
    # Вывод отсортированной таблицы в консоль


    points = {
        'А': Point('А'),
        'Б': Point('Б'),
        'В': Point('В')
    }

    for _, row in df.iterrows():
        point_receipt = row['Пункт приема']
        point_delivery = row['Пункт выдачи']

        day_receipt = row['День приема заказа']
        day_departure = row['День отбытия со склада приема']
        day_arrival = row['День прибытия на склад выдачи']
        day_issuance = row['День выдачи']

        preparation_time = day_departure - day_receipt
        transportation_from_time = day_arrival - day_departure
        points[point_receipt].add_preparation_time((day_receipt, preparation_time))
        points[point_receipt].add_transportation_from_time((day_departure, transportation_from_time))

        transportation_to_time = day_arrival - day_departure
        issuance_time = day_issuance - day_arrival
        points[point_delivery].add_transportation_to_time((day_arrival, transportation_to_time))
        points[point_delivery].add_issuance_time((day_arrival, issuance_time))

    return points
