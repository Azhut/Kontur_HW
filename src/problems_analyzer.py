def analyze_delivery_issues(points):
    """
    Анализирует данные по времени подготовки, транспортировки и выдачи для пунктов A, Б и В
    и находит отклонения в среднем времени за последние 14 и 30 дней

    :param points: Словарь объектов Point
    :return: Пункт с наибольшими отклонениями по времени
    """
    report = {}

    for point_name, point in points.items():
        averages = point.calculate_averages()

        problems = point.analyze_problems(averages)
        if problems:
            report[point_name] = problems

    for point_name, problems in report.items():
        print(f"Проблемы в пункте {point_name}:")
        for problem in problems:
            print(f"- {problem}")
        print()

    if report:
        most_problems_point = max(report, key=lambda x: len(report[x]))
        print(f"Пункт с наибольшими проблемами: {most_problems_point}")
    else:
        print("Проблемы не обнаружены")

