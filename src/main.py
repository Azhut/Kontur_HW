from src.excel_processor import process_excel
from src.plotter import plot_data

def main():
    file_path = '../data/data.xlsx'
    points = process_excel(file_path)
    plot_data(points)

if __name__ == "__main__":
    main()
