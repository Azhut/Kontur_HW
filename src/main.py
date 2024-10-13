from src.excel_processor import process_excel
from src.plotter import plot_data
from src.problems_analyzer import analyze_delivery_issues


def main():
    file_path = '../data/data.xlsx'
    points = process_excel(file_path)
    analyze_delivery_issues(points)
    plot_data(points)

if __name__ == "__main__":
    main()
