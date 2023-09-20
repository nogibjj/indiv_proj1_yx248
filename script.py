# script.py

from lib import load_data, get_descriptive_statistics, plot_data_distribution

def main():
    data = load_data()
    stats = get_descriptive_statistics(data)
    print(stats)
    plot_data_distribution(data, "Price")

if __name__ == "__main__":
    main()
