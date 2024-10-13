class Point:
    """
    Класс для хранения данных о пункте приема\выдачи расчета среднего времени
    """

    def __init__(self, name):
        """
        Инициализация объекта пункта.

        :param name: Название пункта (например, А, Б, В).
        """
        self.name = name
        self.preparation_times = []
        self.transportation_from_times = []
        self.transportation_to_times = []
        self.issuance_times = []

    def add_preparation_time(self, time):
        """Добавление времени подготовки."""
        self.preparation_times.append(time)

    def add_transportation_from_time(self, time):
        """Добавление времени транспортировки из пункта."""
        self.transportation_from_times.append(time)

    def add_transportation_to_time(self, time):
        """Добавление времени транспортировки до пункта."""
        self.transportation_to_times.append(time)

    def add_issuance_time(self, time):
        """Добавление времени выдачи."""
        self.issuance_times.append(time)

    def get_average(self, times_list, days_range):
        """
        Вычисление среднего времени по указанному диапазону дней

        :param times_list: Список времен для вычисления среднего.
        :param days_range: Диапазон дней для фильтрации данных.
        :return: Среднее время.
        """
        filtered_times = [t for t in times_list if t[0] in days_range]
        if filtered_times:
            return sum(t[1] for t in filtered_times) / len(filtered_times)
        return 0

    def calculate_averages(self):
        """
        Вычисление всех средних времен за 30 и 14 дней

        :return: Словарь со средними временами
        """
        last_30_days = range(1, 32)
        last_14_days = range(16, 32)

        return {
            'preparation_30_days': self.get_average(self.preparation_times, last_30_days),
            'preparation_14_days': self.get_average(self.preparation_times, last_14_days),
            'transportation_from_30_days': self.get_average(self.transportation_from_times, last_30_days),
            'transportation_from_14_days': self.get_average(self.transportation_from_times, last_14_days),
            'transportation_to_30_days': self.get_average(self.transportation_to_times, last_30_days),
            'transportation_to_14_days': self.get_average(self.transportation_to_times, last_14_days),
            'issuance_30_days': self.get_average(self.issuance_times, last_30_days),
            'issuance_14_days': self.get_average(self.issuance_times, last_14_days)
        }
