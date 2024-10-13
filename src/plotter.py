import matplotlib.pyplot as plt
import numpy as np

def plot_data(points):
    """
    Построение диаграмм для каждого пункта.

    :param points: Словарь объектов Point.
    """

    colors_30_days = ['#3498db', '#1abc9c', '#9b59b6', '#e74c3c']  # Стили для 30 дней
    colors_14_days = ['#2980b9', '#16a085', '#8e44ad', '#c0392b']  # Стили для 14 дней

    for point_name, point in points.items():
        labels = ['Прием', f'Транспортировка из пункта {point_name}', f'Транспортировка до пункта {point_name}', 'Выдача']
        averages = point.calculate_averages()

        data_30 = [
            averages['preparation_30_days'],
            averages['transportation_from_30_days'],
            averages['transportation_to_30_days'],
            averages['issuance_30_days']
        ]

        data_14 = [
            averages['preparation_14_days'],
            averages['transportation_from_14_days'],
            averages['transportation_to_14_days'],
            averages['issuance_14_days']
        ]

        x = np.arange(len(labels))
        width = 0.35

        fig, ax = plt.subplots(figsize=(10, 6))

        bars_30 = ax.bar(x - width/2, data_30, width, label='Первые 16 днем месяца', color=colors_30_days)
        bars_14 = ax.bar(x + width/2, data_14, width, label='Последние 14 дней', color=colors_14_days)

        ax.set_xlabel('Категории')
        ax.set_ylabel('Среднее время (дни)')
        ax.set_title(f'Статистика для Пункта {point_name}')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()

        for bars in [bars_30, bars_14]:
            for bar in bars:
                yval = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

        plt.tight_layout()
        plt.show()
