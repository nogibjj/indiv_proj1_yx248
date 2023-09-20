# test_lib.py
from lib import load_data, get_descriptive_statistics

def test_load_data():
    data = load_data()
    assert not data.empty, "Data loaded is empty!"

def test_get_descriptive_statistics():
    data = load_data()
    stats = get_descriptive_statistics(data)
    assert "mean" in stats.index, "Means not calculated!"
