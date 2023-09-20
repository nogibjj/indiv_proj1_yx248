from lib import load_data, get_descriptive_statistics, plot_data_distribution

def test_script_main_logic():
    data = load_data()
    assert not data.empty, "Data loaded is empty!"

    stats = get_descriptive_statistics(data)
    assert "mean" in stats.index, "Means not calculated!"

    # Since plotting just shows the figure, we can potentially check for errors by running the function.
    # But we can't assert on matplotlib figures easily without a lot of additional code.
    try:
        plot_data_distribution(data, "Price", save=False)
    except Exception as e:
        assert False, f"Plotting failed with error: {e}"
